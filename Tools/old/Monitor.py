# encoding: utf-8
"""
@author: fonttian
@contact: fonttian@gmail.com
@license: by-nc-sa
@file: Monitor.py
@time: 2020/8/27 下午2:11
"""
from Tools.old.RedisTools import redis_hset


def node_monitor(redis_hashmap_name, stage, code_list):
    code_list.insert(
        0, redis_hset(redis_hashmap_name, stage, "运行中", 0, value_is_str=True)
    )
    code_list.append(
        redis_hset(
            redis_hashmap_name,
            stage,
            "完成",
            0,
            value_is_str=True))
    return code_list


def metrics_hset(redis_hashmap_name, metrics_list):
    return_list = []

    key_list = ["模型训练分数", "模型测试分数"]
    len_key_list = len(key_list)
    for i in range(len(metrics_list)):
        if i < len_key_list:
            return_list.append(
                redis_hset(redis_hashmap_name, key_list[i], metrics_list[i], 0, value_is_str=False)
            )
        else:
            return_list.append(
                redis_hset(redis_hashmap_name, "评估函数" + metrics_list[i] + "数值", "score_test_" + metrics_list[i], 0, value_is_str=False)
            )

    return return_list


def var_hset(redis_hashmap_name, var_key, var_str):
    return redis_hset(redis_hashmap_name, var_key, var_str, space=0, value_is_str=False)
