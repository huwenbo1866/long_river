# encoding: utf-8
"""
@author: fonttian
@contact: fonttian@gmail.com
@license: by-nc-sa
@file: CodeGenerator_Applications.py
@time: 2020/7/1 下午1:29
"""
import gc

from Tools import work_path
from Tools.JSONParser import (
    get_json_from_json_group,
    get_compile_from_json,
    detect_brackets, get_compile_from_json_for_app,
)
from Tools.Writer import code_writer, code_clear_writer, end_of_line_character_handling

global hasTestDataset


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
    return model_dataset(json)


# 生成应用代码
def applications(json):
    result_list = [
        "strategy = tf.distribute.MirroredStrategy()",
        "with strategy.scope():",
        "    model = {net}(weights=None,input_shape={input_shape},classes={classes})".format_map(
            json["params"]),
    ]
    return result_list


# 生成应用代码
def applications_code_generator(json_group):
    json = get_json_from_json_group(json_group, 3, "applications")
    return applications(json)


# 生成模型编译代码
def model_compile(dic):
    result_string = (
            "    model.compile(optimizer=keras.optimizers." +
            dic["optimizer"]["fun"] +
            "(")

    if dic["optimizer"]["params"]:
        for item in dic["optimizer"]["params"]:
            result_string += item + "=" + \
                             dic["optimizer"]["params"][item] + ","

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


# 生成模型编译代码
def compile_code_generator(json_group):
    result_list = [
        model_compile(get_compile_from_json_for_app(json_group)),
    ]

    return result_list


# 生成模型训练代码
def model_fit(json):
    result_string = "model." + json["fun"] + "(train_dataset,"
    for item in json["params"]:
        result_string += item + "=" + json["params"][item] + ","

    result_string += ")"

    return result_string


# 生成模型训练代码
def FitCodeGenerator(json_group):
    json = get_json_from_json_group(json_group, 7)
    result_list = [
        model_fit(json),
    ]

    return result_list


# 生成模型评估代码
def model_evaluate(json, json_list):
    string = "evaluate_loss"
    evaluate_list = ["evaluate_loss"]
    for item in json_list:
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


# 生成模型评估代码
def evaluate_code_generator(json_group):
    dic = get_compile_from_json(json_group)

    json = get_json_from_json_group(json_group, 8, "evaluate")

    result_list = []

    l1 = dic["metrics"]["params"]["metrics"].split(" ")
    model_evaluate_list, evaluate_list = model_evaluate(json, l1)
    result_list.extend(model_evaluate_list)

    return result_list


# 生成模型保存代码
def model_save(json):
    result_string = (
            'model.save("' + work_path + '{path}/{name}.h5")'.format_map(json["params"])
    ).replace("//", "/")

    return result_string


# 生成模型保存代码
def save_code_generator(json_group):
    json = get_json_from_json_group(json_group, 9, "name")
    if json is None:
        return json
    result_list = [
        model_save(json),
    ]

    return result_list


# 获取导入代码
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

    def get_net():
        json = get_json_from_json_group(json_group, 3, "applications")
        return json["params"]["net"]

    net = get_net()
    net_list = [
        "from tensorflow.python.keras.applications.densenet import DenseNet121, DenseNet169, DenseNet201",
        "from tensorflow.python.keras.applications.inception_resnet_v2 import InceptionResNetV2",
        "from tensorflow.python.keras.applications.mobilenet import MobileNet",
        "from tensorflow.python.keras.applications.mobilenet_v2 import MobileNetV2",
        "from tensorflow.python.keras.applications.nasnet import NASNetLarge",
        "from tensorflow.python.keras.applications.resnet import *",
        "from tensorflow.python.keras.applications.resnet_v2 import ResNet50V2, ResNet101V2, ResNet152V2",
        "from tensorflow.python.keras.applications.vgg16 import VGG16",
        "from tensorflow.keras.applications.resnet50 import ResNet50",
        "from tensorflow.python.keras.applications.vgg19 import VGG19",
        "from tensorflow.python.keras.applications.xception import Xception",
        "from tensorflow.python.keras.preprocessing.image_classification import ImageDataGenerator",
    ]

    get_net = ""
    for i in net_list:
        if net in i.split(" "):
            get_net = i

    import_list = [
        "import tensorflow as tf",
        "import tensorflow.keras as keras",
        get_data_reader,
        get_net,
    ]

    return import_list


# 生成代码前的导入代码
def __json2applications_controller_before(json_group):
    result_list = get_import_code(json_group)
    return result_list


# 生成代码
def json2applications_controller(project_name, json_group, bl_run_generate_code=1):
    try:

        list_code_before = __json2applications_controller_before(json_group)

        list_code = DataSetCodeGenerator(json_group)
        list_code.extend(applications_code_generator(json_group))
        list_code.extend(compile_code_generator(json_group))
        list_code.extend(FitCodeGenerator(json_group))
        list_code.extend(evaluate_code_generator(json_group))

        # save 为可选
        if not save_code_generator(json_group) is None:
            list_code.extend(save_code_generator(json_group))

        import os

        py_file = "generate_code_applications.py"

        try:
            code_writer(py_file, list_code_before, list_code)
        except Exception as e:
            print("运行中断，写入临时代码阶段出现运行异常: ", str(e))

        # 手动垃圾回收
        gc.collect()

        try:
            return_dic = code_clear_writer(project_name, "applications", "applications")
        except Exception as e:
            print(e)
            print("运行中断，写入项目代码阶段出现运行异常")

        while bl_run_generate_code:
            if os.path.exists(py_file):
                from generate_code_applications import generator_code
                try:
                    generator_code()
                except Exception as e:
                    print("生成代码, 运行出现运行异常: ", str(e))
                    return 0
            return 0
    except Exception as e:
        print("生成与运行代码时，出现运行异常: ", str(e))
