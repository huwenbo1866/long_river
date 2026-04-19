# encoding: utf-8
"""
@author: fonttian
@contact: fonttian@gmail.com
@license: by-nc-sa
@file: JSONParser.py
@time: 2020/7/27 下午2:10
"""


class JsonParser:
    def __int__(self, str_json):
        self.json = str_json

    def get_countJson(self):
        return self.json['countJson']


def detect_brackets(string):
    string = string.replace(" ", "")
    if string[-2:] == "()":
        return string
    else:
        return string + "()"


def get_json_from_json_group(json_group, index=None, name=None):
    if index is not None:
        for item in json_group:
            if item["pipelineIndex"] == str(index):
                return item
    else:
        for item in json_group:
            if item["pipelineIndex"] == index and item["name"] == name:
                return item
    return None


def get_dict_from_json(json_group, index=None, name=None):
    dic = {}
    for item in json_group:
        if item["pipelineIndex"] == str(index) and item["name"] == name:
            dic.update({item["groupIndex"]: item})
    return dic


def get_compile_from_json(json_group):
    dic = {}
    for item in json_group:
        if item["pipelineIndex"] == "4" and item["name"] == "optimizer":
            dic.update({"optimizer": item})
        if item["pipelineIndex"] == "5" and item["name"] == "loss":
            dic.update({"loss": item})
        if item["pipelineIndex"] == "6" and item["name"] == "metrics":
            dic.update({"metrics": item})
    return dic


def get_compile_from_json_for_app(json_group):
    dic = {}
    for item in json_group:
        if item["pipelineIndex"] == "4":
            dic.update({"optimizer": item})
        if item["pipelineIndex"] == "5":
            dic.update({"loss": item})
        if item["pipelineIndex"] == "6":
            dic.update({"metrics": item})
    return dic


# 2.0
def get_node_by_pipeline_index(json_array, json_id):
    for item in json_array:
        if item["pipelineIndex"] == str(json_id):
            return item


def get_node_by_id(json_array, json_id):
    for item in json_array:
        if item["connection"]["id"] == str(json_id):
            return item


def get_values_map_in_space_by_internal_name(node_space):
    return {i['internal_name']: get_real_values(i['values']) for i in node_space}


def get_next_id_by_id(json_array, now_id):
    return get_node_by_id(json_array, now_id)["connection"]["followers"][0]


def get_node_by_index(json_array, index):
    return get_node_by_id(json_array, get_node_id_by_index(json_array, index)[0])


def get_node_id_by_index(json_array, index):
    id_list = []
    following_id_list = []
    for i in json_array:
        if i["connection"]["index"] == str(index):
            id_list.append(i["connection"]["id"])
            following_id_list.append(i["connection"]["following"][0])

    start_id = id_list[following_id_list.index(list(set(following_id_list) - set(id_list))[0])]

    return_list = []
    for i in range(len(id_list)):
        return_list.append(start_id)
        start_id = get_next_id_by_id(json_array, start_id)

    return return_list


def get_id_by_index_list(json_array, index_list):
    return_list = []
    for i in json_array:
        if i["connection"]["index"] in index_list:
            return_list.append(i["connection"]["id"])
    return_list.sort()  
    # 前端保证按照单元的前后顺序给id重新赋值，此处可保证生成代码顺序等于用户给出的单元排序
    return return_list


def get_starting_node(json_array):
    for item in json_array:
        if item["connection"]["following"] == ["starting_node"]:
            return item, item["connection"]["followers"]


def get_internal_name_values_from_parameter(config, internal_name):
    for item in config:
        if item["internal_name"] == internal_name:
            return item["values"]


def get_values_type(values):
    values_list = values.split(":")
    return values_list[0]


def get_real_values(values):
    """
    根据值的类型返回实际值。
    如果是字符串或单选类型，返回带引号的字符串。
    否则，返回去掉类型前缀的值。
    """
    if not isinstance(values, str):
        values = values[0]
    values_list = values.split(":")
    if values_list[0] == "str" or values_list[0] == "single_choice":
        return '"' + values.replace(values_list[0] + ":", "") + '"'
    else:
        return values.replace(values_list[0] + ":", "")


def config2dict(node):
    """
    将配置节点转换为字典。
    遍历节点中的参数，将内部名称和实际值添加到字典中。
    """
    return_dict = {}
    for item in node["parameter"]:
        return_dict.update(
            {item["internal_name"]: get_real_values(item["values"])})
    return return_dict


def config2str(node):
    """
    将配置节点转换为字符串。
    遍历节点中的参数，根据值的类型生成相应的字符串表示。
    """
    return_str = ""
    for item in node["parameter"]:
        values_type = get_values_type(item["values"])
        if values_type not in ["estimator", "estimator_list", "url"]:
            return_str += (item["internal_name"] + "=" +
                           get_real_values(item["values"]) + ", ")
        elif values_type in ["url"]:
            return_str += (item["internal_name"] + '="' +
                           get_real_values(item["values"]) + '", ')
        elif values_type in ["estimator"]:
            return_str += (
                    item["internal_name"]
                    + "="
                    + item["values"]["func"]
                    + "("
                    + config2str(item["values"])
                    + "), "
            )
        else:
            return_str += "["
            for jItem in item["values"]:
                return_str += (
                        '("'
                        + jItem["func"]
                        + "_"
                        + jItem["connection"]["id"]
                        + ", "
                        + config2str(jItem["values"])
                        + "),"
                )
            return_str += "],"
            
    return return_str


def get_internal_name_by_node(node):
    return_str = ""
    for item in node["parameter"]:
        values_type = get_values_type(item["internal_name"])
        if values_type not in ["estimator", "estimator_list", "url"]:
            if get_real_values(item["values"]) == "":
                pass
            else:
                return_str += (item["internal_name"] + "=" +
                               get_real_values(item["values"]) + ", ")
        elif values_type in ["url"]:
            return_str += (item["internal_name"] + '="' +
                           get_real_values(item["values"]) + '", ')
        elif values_type in ["estimator"]:
            return_str += (
                    item["internal_name"]
                    + "="
                    + item["values"]["func"]
                    + "("
                    + get_internal_name_by_node(item["values"])
                    + "), "
            )
        else:
            return_str += "["
            for jItem in item["values"]:
                return_str += (
                        '("'
                        + jItem["func"]
                        + "_"
                        + jItem["connection"]["id"]
                        + ", "
                        + get_internal_name_by_node(jItem["values"])
                        + "),"
                )
            return_str += "],"

    return return_str


def get_next_id(json_array, json_id):
    while json_id != "end_node":
        yield json_id
        json_id = get_node_by_id(json_array, json_id)[
            "connection"]["followers"][0]


def get_all_id_list(json_array, next_id):
    return_list = []
    for item in next_id:
        return_list.append(list(get_next_id(json_array, item)))
    return return_list[0]
