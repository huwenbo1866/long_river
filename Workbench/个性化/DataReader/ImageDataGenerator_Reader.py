# encoding: utf-8
"""
@author: fonttian
@contact: fonttian@gmail.com
@license: by-nc-sa
@file: ImageDataGenerator_Reader.py
@time: 2020/7/8 上午10:01
"""
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
from Tools import work_path


def flow_from_directory_basis_function(
        path,
        img_height=128,
        img_width=128,
        batch_size=32,
        class_mode="categorical"):
    train_data_gen = ImageDataGenerator()

    train_generator = train_data_gen.flow_from_directory(
        directory=path,
        target_size=(img_height, img_width),
        batch_size=batch_size,
        class_mode=class_mode,
    )

    return train_generator


def flow_from_directory(
        path,
        has_test=False,
        img_height=128,
        img_width=128,
        class_mode="categorical"):
    path = (work_path + path).replace("//", "/")
    if not has_test:
        return flow_from_directory_basis_function(
            path=path,
            img_height=img_height,
            img_width=img_width,
            class_mode=class_mode)
    else:
        return flow_from_directory_basis_function(
            path=path + "/train",
            img_height=img_height,
            img_width=img_width,
            class_mode=class_mode,
        ), flow_from_directory_basis_function(
            path + "/test",
            img_height=img_height,
            img_width=img_width,
            class_mode=class_mode,
        )
