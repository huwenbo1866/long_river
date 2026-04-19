# encoding: utf-8
"""
@author: fonttian
@contact: fonttian@gmail.com
@license: by-nc-sa
@file: CodeGenerator_AutoML.py
@time: 2020/7/7 上午9:03
"""
import gc

from Tools import work_path
from Tools.JSONParser import get_json_from_json_group
from Tools.Writer import code_writer, code_clear_writer, end_of_line_character_handling

global hasTestDataset
global model_type
global redisHashMappingName


# 根据json生成数据集代码
def model_dataset(json):
    global hasTestDataset
    result_list = []
    if json["fun"] in [
        "images_dir",
        "text_dir",
        "numpy_reader",
        "csv_pandas_dir",
        "flow_from_directory",
    ]:
        if json["params"]["hasTest"] == "True" or "take_size" not in list(
                json["params"].keys()
        ):
            string = "train_dataset = " + json["fun"] + "("
            hasTestDataset = False
        else:
            hasTestDataset = True
            string = "train_dataset, test_dataset = " + json["fun"] + "("

        for item in json["params"]:
            if item in ["path", "class_mode"]:
                string += item + '="' + json["params"][item] + '", '
            else:
                string += item + "=" + json["params"][item] + ", "
        string = end_of_line_character_handling(string)
        result_list.append(string)
    elif json["fun"] == "csv_dir":
        if json["params"]["hasTest"] == "True":
            hasTestDataset = True
            result_list.append(
                "train_path,test_path = "
                + json["fun"]
                + '(path="'
                + json["params"]["path"].replace("//", "/")
                + '")'
            )
        else:
            hasTestDataset = False
            result_list.append(
                "train_path = "
                + json["fun"]
                + '(path="'
                + json["params"]["path"].replace("//", "/")
                + '")'
            )

    return result_list


# 生成数据集代码
def DataSetCodeGenerator(json_group):
    json = get_json_from_json_group(json_group, 1)
    result_list = model_dataset(json)
    return result_list


# 根据json生成AutoML代码
def automl(json):
    global model_type
    model_json = {
        "enas_images_classification": "ImageClassifier",
        "enas_images_regression": "ImageRegressor",
        "enas_text_classification": "TextClassifier",
        "enas_text_regression": "TextRegressor",
        "enas_structured_data_classification": "StructuredDataClassifier",
        "enas_structured_data_regression": "StructuredDataRegressor",
        "TPOT_structured_data_classification": "TPOTClassifier",
        "TPOT_structured_data_regression": "TPOTRegressor",
    }
    result_list = []
    autokeras_model_list = [
        "enas_images_classification",
        "enas_images_regression",
        "enas_text_classification",
        "enas_text_regression",
        "enas_structured_data_classification",
        "enas_structured_data_regression",
    ]

    autokeras_model_list_sd = [
        "enas_structured_data_classification",
        "enas_structured_data_regression",
    ]

    if json["fun"] in autokeras_model_list:
        model_type = "autokeras"
        result_list.append("import autokeras as ak")
        create_model_string = "model = ak.{model}(".format_map(
            {"model": model_json[json["fun"]]}
        )
        if json["fun"] in autokeras_model_list_sd:
            fit_model_string = "model.fit(train_path, "
            model_type = "autokeras_sd"
        else:
            fit_model_string = "model.fit(train_dataset, "
        for item in json["params"]:
            if item in ["max_trials", "overwrite", "seed"]:
                create_model_string += item + "=" + json["params"][item] + ", "
            if item in ["loss"]:
                create_model_string += item + '="' + \
                                       json["params"][item] + '", '
            if item in ["metrics"]:
                create_model_string += item + \
                                       '=["' + json["params"][item] + '"], '

            if item in ["validation_split", "epochs"]:
                fit_model_string += item + "=" + json["params"][item] + ", "
            if item == "validation_data" and hasTestDataset:
                fit_model_string += "validation_data=test_dataset, "
            if item in ["y"]:
                fit_model_string += item + '="' + json["params"][item] + '", '
        result_list.append(end_of_line_character_handling(create_model_string))
        result_list.append(end_of_line_character_handling(fit_model_string))

    if json["fun"] in ["TPOTClassifier", "TPOTRegressor"]:
        model_type = "tpot"
        result_list.append("from tpot import TPOTClassifier,TPOTRegressor")
        from ModelCreator.tpot import get_data_list

        test_size, dataset_split_random_state = "0.2", "42"
        if "test_size" in list(json["params"].keys()):
            test_size = json["params"]["test_size"]
        if "dataset_split_random_state" in list(json["params"].keys()):
            dataset_split_random_state = json["params"]["dataset_split_random_state"]
        data_list = get_data_list(
            labels=json["params"]["labels"],
            has_test=hasTestDataset,
            test_size=float(test_size),
            random_state=float(dataset_split_random_state),
        )

        create_model_string = "pipeline_optimizer = " + json["fun"] + "("
        fit_model_string = "pipeline_optimizer.fit(X_train, y_train)"
        for item in json["params"]:
            if item in ["cv_split_random_state"]:
                create_model_string += "random_state=" + \
                                       json["params"][item] + ", "
            if item in [
                "epochs",
                "generations",
                "population_size",
                "cv",
                "early_stop",
                "n_jobs",
            ]:
                create_model_string += item + "=" + json["params"][item] + ", "
            if item in ["scoring"]:
                create_model_string += item + '="' + \
                                       json["params"][item] + '", '
        if "n_jobs" not in list(json["params"].keys()):
            create_model_string += "n_jobs=-1, "
        result_list.extend(data_list)
        result_list.append(end_of_line_character_handling(create_model_string))
        result_list.append(fit_model_string)

    return result_list


def AutoMLCodeGenerator(json_group):
    json = get_json_from_json_group(json_group, 3, "model")
    result_list = automl(json)
    return result_list


def model_evaluate():
    result_list = []
    if model_type == "autokeras":
        if hasTestDataset:
            result_list.append("evaluate = model.evaluate(test_dataset)")
        else:
            result_list.append("evaluate = model.evaluate(train_dataset)")
    if model_type == "autokeras_sd":
        if hasTestDataset:
            result_list.append("evaluate = model.evaluate(test_path)")
        else:
            result_list.append("evaluate = model.evaluate(train_path)")
    if model_type == "tpot":
        if hasTestDataset:
            result_list.append(
                "evaluate = pipeline_optimizer.score(X_test, y_test)")
        else:
            result_list.append(
                "evaluate = pipeline_optimizer.score(X_train, y_train)")

    return result_list


def EvaluateCodeGenerator(json_group):
    json = get_json_from_json_group(json_group, 4, "evaluate")
    if json is None:
        return json

    return model_evaluate()


def model_save(json):
    result_list = []
    if model_type in ["autokeras", "autokeras_sd"]:
        file = json["params"]["filepath"]
        if json["params"]["save_format"] == "h5":
            file += ".h5"
        result_list.append("model_save = model.export_model()")
        result_list.append(
            'model_save.save("'
            + (work_path + file).replace("//", "/")
            + '", save_format= "'
            + json["params"]["save_format"]
            + '" )'.replace("//", "/")
        )

    if model_type in ["tpot"]:
        result_list.append(
            (
                    'pipeline_optimizer.export("'
                    + work_path
                    + json["params"]["filepath"]
                    + '.py")'
            ).replace("//", "/")
        )

    return result_list


def SaveCodeGenerator(json_group):
    json = get_json_from_json_group(json_group, 5, "save")
    if json is None:
        return json
    result_list = model_save(json)

    return result_list


def get_import_code(json_group):
    def get_data_reader():
        json = get_json_from_json_group(json_group, 1, "datasetReader")
        return json["fun"]

    data_reader_list = [
        "from DataReader.ImageDataGenerator_Reader import flow_from_directory",
        "from DataReader.TFDS import images_dir",
        "from DataReader.TFDS import text_dir",
        "from DataReader.TFDS import numpy_reader",
        "from DataReader.TFDS import csv_pandas_dir",
        "from DataReader.Parser import csv_dir",
        "from DataReader.PythonML import load_data_by_csv",
        "from DataReader.PythonML import load_data_by_pandas",
        "from DataReader.PythonML import download_data_by_pandas",
    ]

    data_reader = get_data_reader()
    get_data_reader = ""
    for i in data_reader_list:
        if data_reader in i.split(" "):
            get_data_reader = i

    import_list = [get_data_reader]

    return import_list


def __json2AutoMLController_before(json_group):
    result_list = get_import_code(json_group)
    return result_list


def json2AutoMLController(project_name, json_group, bl_run_generate_code=True):
    global redisHashMappingName
    redis_json = get_json_from_json_group(json_group, 0)

    try:

        list_code_before = __json2AutoMLController_before(json_group)

        list_code = []
        list_code.extend(DataSetCodeGenerator(json_group))
        list_code.extend(AutoMLCodeGenerator(json_group))

        # evaluate , save 为可选
        if not EvaluateCodeGenerator(json_group) is None:
            list_code.extend(EvaluateCodeGenerator(json_group))
        if not SaveCodeGenerator(json_group) is None:
            list_code.extend(SaveCodeGenerator(json_group))

        import os

        try:
            py_file = "generate_code_automl.py"
            code_writer(py_file, list_code_before, list_code)
        except Exception as e:
            print("运行中断，写入临时代码阶段出现运行异常: ", str(e))

        # 手动垃圾回收
        gc.collect()

        try:
            return_dic = code_clear_writer(project_name, "automl", "automl")
        except Exception as e:
            print(e)
            print("运行中断，写入项目代码阶段出现运行异常")

        while bl_run_generate_code:
            if os.path.exists(py_file):
                from generate_code_automl import generator_code
                try:
                    generator_code()
                except Exception as e:
                    print("生成代码, 运行出现运行异常: ", str(e))
                    return 0
                return 0
    except Exception as e:
        print("生成与运行代码时，出现运行异常: ", str(e))
