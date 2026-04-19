# encoding: utf-8
"""
@author: fonttian
@contact: fonttian@gmail.com
@license: by-nc-sa
@file: tpot.py
@time: 2020/7/8 下午3:43
"""


def get_data_list(labels, has_test=False, test_size=0.2, random_state=42):
    if has_test:
        data_list = [
            "import pandas as pd",
            "X_train = pd.read_csv(train_path)",
            'labels = "' + labels + '"',
            "y_train = X_train.pop(labels)",
            "X_test = pd.read_csv(test_path)",
            "y_test = X_train.pop(labels)",
        ]
        return data_list
    else:
        data_list = [
            "from sklearn.model_selection import train_test_split",
            "import pandas as pd",
            "tpot_data = pd.read_csv(train_path)",
            'target = tpot_data.pop("' +
            labels +
            '")',
            "X_train, X_test, y_train, y_test = train_test_split(tpot_data.values, target.values, test_size=" +
            str(test_size) +
            ", random_state=" +
            str(random_state) +
            ")",
        ]

        return data_list
