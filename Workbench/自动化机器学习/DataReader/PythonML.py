# encoding: utf-8
"""
@author: FontTian
@contact: fonttian@gmail.com
@license: by-nc-sa
@file: PythonML.py
@time: 2020/7/17 下午2:26
"""
import pandas as pd
import numpy as np
from Tools import work_path
import csv
from os.path import join


def load_data_by_csv(module_path, data_file_name):
    """Loads data from module_path/data_file_name.

    Parameters
    ----------
    module_path : string
        The module path.

    data_file_name : string
        Name of csv file to be loaded from
        module_path/data/data_file_name. For example 'wine_data.csv'.

    Returns
    -------
    data : Numpy array
        A 2D array with each row representing one sample and each column
        representing the features of a given sample.

    target : Numpy array
        A 1D array holding target variables for all the samples in `data.
        For example target[0] is the target variable for data[0].

    target_names : Numpy array
        A 1D array containing the names of the classifications. For example
        target_names[0] is the name of the target[0] class.
    """
    with open(
        join((work_path + module_path).replace("//", "/"), data_file_name)
    ) as csv_file:
        data_file = csv.reader(csv_file)
        temp = next(data_file)
        n_samples = int(temp[0])
        n_features = int(temp[1])
        target_names = np.array(temp[2:])
        data = np.empty((n_samples, n_features))
        target = np.empty((n_samples,), dtype=np.int)

        for i, ir in enumerate(data_file):
            data[i] = np.asarray(ir[:-1], dtype=np.float64)
            target[i] = np.asarray(ir[-1], dtype=np.int)

    return data, target, target_names


def load_data_by_pandas(
    filepath, index_col=None, header="infer", delimiter=None, labels="target"
):
    data_file = pd.read_csv(
        filepath_or_bufferstr=(work_path + filepath).replace("//", "/"),
        index_col=index_col,
        header=header,
        delimiter=delimiter,
    )
    y = np.array(data_file.quality)
    x = np.array(data_file.drop(labels, axis=1))
    columns = np.array(data_file.columns)

    return x, y, columns


def download_data_by_pandas(
    url, index_col=None, header="infer", delimiter=None, labels="target"
):
    data_file = pd.read_csv(
        url, index_col=index_col, header=header, delimiter=delimiter
    )
    if labels is None:
        y = np.array(data_file.iloc[:, -1])
        len_df = data_file.shape[1]
        x = np.array(data_file.drop([len_df - 2, len_df - 1], axis=1))
    else:
        y = np.array(data_file[labels])
        x = np.array(data_file.drop(labels, axis=1))

    return x, y
