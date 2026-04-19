# encoding: utf-8
"""
@author: fonttian
@contact: fonttian@gmail.com
@license: by-nc-sa
@file: PaddleBuilder.py
@time: 2021/3/4 上午10:37
"""
from Tools.JSONParser import (
    get_node_by_id,
    get_real_values,
    get_internal_name_by_node, get_node_id_by_index,
    get_values_map_in_space_by_internal_name
)


def import_builder(json_array):
    # 导入需要的库
    return_list = [
        "import paddle",
        "import cv2",
        "import random",
        "import numpy as np",
        "import os",
        "import paddle.vision.transforms as T",
        "from DataReader.PaddlePaddle import data_loader"
    ]

    # 导入json_array中id为0的节点
    return_list.extend(get_node_by_id(json_array, "0"))

    return return_list


def data_reader_builder(json_array):
    # 获取json_array中id为1的节点
    node = get_node_by_id(json_array, get_node_id_by_index(json_array, 1)[0])
    # 获取节点的参数
    format_dict = get_values_map_in_space_by_internal_name(node['parameter'], )
    # 构建训练数据加载器
    return_list_of_data_reader = [
        "train_data_loader = data_loader(\"{}\", transform_img=transform(),batch_size={},shuffle={})".format(
            format_dict['train_loader_path'], format_dict['train_loader_batch_size'],
            format_dict['train_loader_shuffle']),
        "train_loader = train_data_loader()"
    ]
    # 如果验证数据加载器的路径不为空，则构建验证数据加载器
    if get_real_values(format_dict['val_loader_path']) != "None":
        return_list_of_data_reader.extend([
            "val_loader_loader = data_loader(\"{}\", transform_img=transform(),batch_size={},shuffle={})".format(
                format_dict['val_loader_path'], format_dict['val_loader_batch_size'],
                format_dict['val_loader_shuffle']),
            "val_loader = val_loader_loader()"
        ])
    return return_list_of_data_reader


def _compose_builder(compose_node):
    # 构建transform的字符串
    return_str = "T." + compose_node['internal_name'] + "(" + get_internal_name_by_node(compose_node) + "),"
    return return_str


def transform_builder(json_array):
    # 获取json_array中id为2的节点
    id_all_list = get_node_id_by_index(json_array, 2)

    # 构建transform的字符串
    return_str = "transform = T.Compose(["
    for i in id_all_list:
        compose_node = get_node_by_id(json_array, i)
        return_str += (_compose_builder(compose_node))
    return_str += "])"

    return [return_str]


def _nn_builder(sequential_node):
    # 构建nn的字符串
    code_str_of_hyperparameter = get_internal_name_by_node(sequential_node)
    code_str_of_nn = "paddle.nn." + sequential_node["internal_name"] + "(" + code_str_of_hyperparameter + ")"
    return code_str_of_nn


def model_builder(json_array):
    # 获取json_array中id为3的节点
    id_list_all = get_node_id_by_index(json_array, 3)
    # 构建nn的字符串
    code_str_of_sequential = "net = paddle.nn.Sequential("
    for i in id_list_all:
        sequential_node = get_node_by_id(json_array, i)
        code_str_of_nn = _nn_builder(sequential_node)
        code_str_of_sequential += code_str_of_nn + ","

    code_str_of_sequential += ")"
    return [code_str_of_sequential, "model = paddle.Model(net)"]


def prepare_builder(json_array):
    # 获取json_array中id为4的节点
    node = get_node_by_id(json_array, get_node_id_by_index(json_array, 4)[0])
    # 获取节点的参数
    format_dict = get_values_map_in_space_by_internal_name(node['parameter'], )
    # 构建prepare的字符串
    return_str = "model.prepare(paddle.optimizer.Adam(parameters=model.parameters()),paddle.nn.{loss}()," \
                 "paddle.metric.{metrics}())".format_map(format_dict)

    return [return_str]


def fit_builder(json_array):
    # 获取json_array中id为5的节点
    node = get_node_by_id(json_array, get_node_id_by_index(json_array, 5)[0])
    # 获取节点的参数
    code_str_of_hyperparameter = get_internal_name_by_node(node)
    # 构建fit的字符串
    return_str = "model.fit(train_loader," + code_str_of_hyperparameter + ")"
    return [return_str]


def evaluate_builder(json_array):
    # 获取json_array中id为6的节点
    node = get_node_by_id(json_array, get_node_id_by_index(json_array, 6)[0])
    # 获取节点的参数
    code_str_of_hyperparameter = get_internal_name_by_node(node)
    # 构建evaluate的字符串
    return_str = "result = model.evaluate(val_loader," + code_str_of_hyperparameter + ")"
    return [return_str]


def _save_builder(sequential_node):
    # 构建save的字符串
    code_str_of_hyperparameter = get_internal_name_by_node(sequential_node)
    code_str_of_nn = "model.save(" + code_str_of_hyperparameter + ")"
    return code_str_of_nn


def save_builder(json_array):
    # 获取json_array中id为7的节点
    id_list_all = get_node_id_by_index(json_array, 7)
    # 构建save的字符串
    return_str_list = []
    for i in id_list_all:
        sequential_node = get_node_by_id(json_array, i)
        return_str_list.append(_save_builder(sequential_node))
    return return_str_list
