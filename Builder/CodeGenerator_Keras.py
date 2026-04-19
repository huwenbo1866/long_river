# encoding: utf-8
"""
@author: fonttian
@contact: fonttian@gmail.com
@license: by-nc-sa
@file: CodeGenerator_Keras.py
@time: 2020/6/9 上午8:36
"""
import gc

from Tools import work_path
from Tools.JSONParser import (
    get_json_from_json_group,
    get_dict_from_json,
    get_compile_from_json,
    detect_brackets, get_compile_from_json_for_app,
)

from Tools.Writer import code_writer, code_clear_writer, end_of_line_character_handling

global model_type
global hasTestDataset
global redisHashMappingName
global hasTensorBoard
import os as os


# 生成数据集代码
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


# 生成模型添加代码
def model_add(json):
    result_string = "model.add(" + "keras.layers." + json["fun"] + "("
    for item in json["params"]:
        if item == "padding":
            result_string += item + '="' + json["params"][item] + '",'
        else:
            result_string += item + "=" + json["params"][item] + ","

    result_string = result_string + "))"

    return result_string


# 生成Sequential模型代码
def SequentialCodeGenerator(json_group):
    dic = get_dict_from_json(json_group, 3, "sequential")
    result_list = [
        "strategy = tf.distribute.MirroredStrategy()",
        "with strategy.scope():",
        "    " + "model = keras.Sequential()",
    ]

    for item in range(len(dic)):
        result_list.append("    " + model_add(dic[str(item + 1)]))

    return result_list


# get compile
def model_compile(dic):
    result_string = (
            "    model.compile(optimizer=keras.optimizers." +
            dic["optimizer"]["fun"] +
            "(")

    if dic["loss"]["params"]["loss"] in [
        "softmax_cross_entropy_with_logits",
        "sparse_softmax_cross_entropy_with_logits",
    ]:
        result_string += "),loss=tf.nn." + dic["loss"]["params"]["loss"] + ""
    else:
        result_string += "),loss=keras.losses." + detect_brackets(
            dic["loss"]["params"]["loss"]
        )

    result_string += ",metrics=["
    for item in dic["metrics"]["params"]["metrics"].split(" "):
        result_string += '"' + item + '",'

    result_string += "])"

    return result_string


def CompileCodeGenerator(json_group):
    result_list = [
        model_compile(get_compile_from_json_for_app(json_group)),
    ]

    return result_list


# get Fit
def TensorBoardCodeGenerator(json):
    global hasTensorBoard
    if json is None:
        hasTensorBoard = False
        return "    "

    hasTensorBoard = True
    result_string = (
        "tbCallBack = keras.callbacks.TensorBoard(log_dir='{logpath}',write_graph={write_graph},"
        "write_grads={write_grads},write_images={write_images})".format_map(
            json["params"]))

    return result_string


def model_fit(json):
    if json["fun"] == "fit":
        result_string = "model.fit(train_dataset,"
    else:
        result_string = "model.fit_generator(train_dataset,"
    for item in json["params"]:
        result_string += item + "=" + json["params"][item] + ","

    if hasTensorBoard:
        result_string += "callbacks=[tbCallBack])"
    else:
        result_string += ")"
    return result_string


def FitCodeGenerator(json_group):
    json = get_json_from_json_group(json_group, 7, "fit")
    result_list = [
        TensorBoardCodeGenerator(
            get_json_from_json_group(json_group, 10, "visualization")
        ),
        model_fit(json),
    ]

    return result_list


def model_evaluate(json, l1):
    string = "evaluate_loss"
    evaluate_list = ["evaluate_loss"]
    for item in l1:
        string += ",evaluate_" + item
        evaluate_list.append("evaluate_" + item)
    if hasTestDataset:
        string += " = model.evaluate(test_dataset,"
    else:
        string += " = model.evaluate(train_dataset,"
    for item in json["params"]:
        if item:
            string += item + "=" + json["params"][item] + ","

    string = string + ")"
    return [string], evaluate_list



def EvaluateCodeGenerator(json_group):
    dic = get_compile_from_json(json_group)

    json = get_json_from_json_group(json_group, 8, "evaluate")


    result_list = []
    l1 = dic["metrics"]["params"]["metrics"].split(" ")
    model_evaluate_list, evaluate_list = model_evaluate(json, l1)
    result_list.extend(model_evaluate_list)

    return result_list


def model_save(json):
    result_string = (
            'model.save("' + work_path + '{path}/{name}.h5")'.format_map(json["params"])
    ).replace("//", "/")

    return result_string


def SaveCodeGenerator(json_group):
    json = get_json_from_json_group(json_group, 9, "name")
    if json is None:
        return json
    result_list = [
        model_save(json),
    ]

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

    import_list = [
        "import tensorflow as tf",
        "import tensorflow.keras as keras",
        "from tensorflow.keras.activations import *",
        get_data_reader,
    ]

    return import_list


def __json2kerasController_before(json_group):
    result_list = get_import_code(json_group)
    return result_list


def json2kerasController(project_name, json_group, bl_run_generate_code=1):

    global redisHashMappingName
    redis_json = get_json_from_json_group(json_group, 0)
    try:
        list_code_before = __json2kerasController_before(json_group)

        list_code = []
        list_code.extend(DataSetCodeGenerator(json_group))
        list_code.extend(SequentialCodeGenerator(json_group))
        list_code.extend(CompileCodeGenerator(json_group))

        list_code.extend(FitCodeGenerator(json_group))
        list_code.extend(EvaluateCodeGenerator(json_group))

        # save 为可选
        if not SaveCodeGenerator(json_group) is None:
            list_code.extend(SaveCodeGenerator(json_group))

        # after
        import os

        # 写入
        py_file = "generate_code_keras.py"
        code_writer(py_file, list_code_before, list_code)

        # 手动垃圾回收
        gc.collect()
    except Exception as e:
        print("运行中断，写入临时代码阶段出现运行异常: ", str(e))

    try:
        try:
            return_dic = code_clear_writer(project_name, "keras", "keras")
        except Exception as e:
            print(e)
            print("运行中断，写入项目代码阶段出现运行异常")

        while bl_run_generate_code:
            if os.path.exists(py_file):
                from generate_code_keras import generator_code
                try:
                    generator_code()
                except Exception as e:
                    print("生成代码, 运行出现运行异常: ", str(e))
                    return 0
                return 0
    except Exception as e:
        print("生成与运行代码时，出现运行异常: ", str(e))
