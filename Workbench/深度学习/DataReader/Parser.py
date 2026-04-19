# encoding: utf-8
"""
@author: fonttian
@contact: fonttian@gmail.com
@license: by-nc-sa
@file: Parser.py
@time: 2020/7/8 上午9:34
"""
from Tools import work_path


def csv_dir(path, has_test=False):
    path = (work_path + path).replace("//", "/")
    train_path = path + "/train.csv"
    if has_test:
        test_path = path + "/test.csv"

        return train_path, test_path
    else:
        return train_path
