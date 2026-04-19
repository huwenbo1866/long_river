# encoding: utf-8
"""
@author: fonttian
@contact: fonttian@gmail.com
@license: by-nc-sa
@file: RedisTools.py
@time: 2020/7/27 下午2:08
"""
from Tools.JSONParser import get_json_from_json_group


def redis_hashmap_name_generator(json_group):
    return get_json_from_json_group(json_group, 0)["params"]["HASH_NAME"]


def redis_clint(json):
    py_redis_code_list = [
        "import redis",
        'pool = redis.ConnectionPool(host="{REDIS_HOST}", port="{REDIS_PORT}", password="{'
        'USER_PWD}")'.format_map(
            json["params"]),
        "redis_client = redis.Redis(connection_pool=pool)",
    ]

    return py_redis_code_list


def redis_client(json):
    py_redis_code_list = [
        "import redis",
        'pool = redis.ConnectionPool(host="{REDIS_HOST}", port="{REDIS_PORT}", password="{'
        'USER_PWD}")'.format_map(json),
        "redis_client = redis.Redis(connection_pool=pool)",
    ]

    return py_redis_code_list


def database_code_generator(json_group):
    json = get_json_from_json_group(json_group, 0)
    result = redis_clint(json)
    return result


def redis_hset(name, key, value, space=1, value_is_str=True):
    if value_is_str:
        return space * "    " + (
            'redis_client.hset("{name}", "{key}", "{value}")\n'.format_map(
                {"name": name, "key": key, "value": value}
            )
        )
    else:
        return space * "    " + (
            'redis_client.hset("{name}", "{key}", {value})\n'.format_map(
                {"name": name, "key": key, "value": value}
            )
        )
