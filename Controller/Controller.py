# encoding: utf-8
"""
@author: fonttian
@contact: fonttian@gmail.com
@license: by-nc-sa
@file: MLBuilder.py
@time: 2020/7/31 上午10:47
"""
import gc

from Builder.MLBuilder import starting_node_builder, pipeline_builder_all, import_builder
from Tools.JSONParser import get_all_id_list, get_node_by_index
from Tools.Writer import code_writer, code_clear_writer

"""
# 整体流程
(1) import_builder -> starting_node_builder -> pipeline_builder_all -> 代码写入模块 -> 执行代码模块
(2) import_builder = 引用 -> redis
(3) starting_node_builder = 数据读取 -> 数据加载（实际执行是：数据加载 -决定-> 数据读取）
(4) pipeline_builder_all = pipeline_model { { 特征处理 + 特征选择 } -> 学习器 } -> 评估 -> 模型保存
(5) 代码写入模块 = code_writer（写入根目录下） + code_clear_writer（复制数据读取文件到work文件夹，对写入文件进行清洗并写入work文件夹）
"""

def ml_controller(project_name, json_array, py_file_name, bl_run_generate_code):
    """
    控制机器学习流程的主函数。

    参数:
    project_name (str): 项目名称。
    json_array (list): 包含节点信息的 JSON 数组。
    py_file_name (str): 生成的 Python 文件名。
    bl_run_generate_code (bool): 是否运行生成的代码。
    """
    list_code_before = []
    list_write_code = []

    try:
        # 生成引用代码
        list_code_before = import_builder(json_array)
        list_code_before.extend([" ", ""])

        # 获取初始节点和下一个节点的 ID
        start_node, next_id = get_start_node_and_next_id(json_array)

        # 创建初始节点生成代码，即数据加载代码
        # 目前采取的先获取数据加载节点，
        # 然后根据数据加载节点中的数据加载方法选择数据读取器
        # 具体实现位于starting_node_builder中

        list_write_code = starting_node_builder(start_node, json_array)
        # 获取全部id的list
        # 实际获取的id是除了数据加载与数据读取外的所有节点的id
        id_list_all = get_all_id_list(json_array, next_id)
        if len(id_list_all) >= 1:
            pipeline_builder_all_code_list = pipeline_builder_all(json_array, id_list_all, )
            list_write_code.extend(pipeline_builder_all_code_list)
        else:
            pass
    except Exception as e:
        print(e)
        print("运行中断，生成代码阶段出现运行异常")


    try:
        # 如果没有传入文件名称参数，则使用默认参数
        if py_file_name is None:
            py_file_name = "generate_code_pyml.py"

        # 手动垃圾回收
        gc.collect()

        # 写入文件
        # print("list_code_before :", list_code_before)
        # print("list_write_code :", list_write_code)
        code_writer(py_file_name, list_code_before, list_write_code, )
    except Exception as e:
        print(e)
        print("运行中断，写入临时代码阶段出现运行异常")

    # return_dic = code_clear_writer(project_name, "pyml", "pyml")

    try:
        return_dic = code_clear_writer(project_name, "pyml", "pyml")
    except Exception as e:
        print(e)
        print("运行中断，写入项目代码阶段出现运行异常")

    try:
        if bl_run_generate_code:
            import os
            if os.path.exists(py_file_name):
                from generate_code_pyml import generator_code
                try:
                    generator_code()
                except Exception as e:
                    print(e)
                    return 0
    except Exception as e:
        print(e)
        print("运行中断，运行代码阶段出现异常")

def get_start_node_and_next_id(json_array):
    """
    获取初始节点和下一个节点的 ID。

    参数:
    json_array (list): 包含节点信息的 JSON 数组。

    返回:
    tuple: 初始节点和下一个节点的 ID。
    """
    start_node = get_node_by_index(json_array, 2)
    next_id = start_node["connection"]['followers'][0]
    return start_node, next_id
