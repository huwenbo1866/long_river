# encoding: utf-8
"""
@author: fonttian
@contact: fonttian@gmail.com
@license: by-nc-sa
@file: TFDS.py
@time: 2020/7/7 下午8:37
"""

import tensorflow as tf
import pathlib
import numpy as np
import os
from Tools import work_path


def images_dir_basis_function(
    path,
    img_height=224,
    img_width=224,
    batch_size=64,
    shuffle_buffer_size=3000,
    take_size=None,
):
    data_dir = pathlib.Path(path)
    CLASS_NAMES = np.array(
        [item.name for item in data_dir.glob("*") if item.name != "LICENSE.txt"]
    )
    list_ds = tf.data.Dataset.list_files(str(data_dir / "*/*"))
    AUTOTUNE = tf.data.experimental.AUTOTUNE

    def get_label(file_path):
        # convert the path to a list of path components
        parts = tf.strings.split(file_path, os.path.sep)
        # The second to last is the class-directory
        return parts[-2] == CLASS_NAMES

    def decode_img(img):
        # convert the compressed string to a 3D int8 tensor
        img = tf.image.decode_jpeg(img, channels=3)
        # Use `convert_image_dtype` to convert to floats in the [0,1] range.
        img = tf.image.convert_image_dtype(img, tf.float32)
        # resize the image_classification to the desired size.
        return tf.image.resize(img, [img_height, img_width])

    def process_path(file_path):
        label = get_label(file_path)
        # load the raw data from the file as a string
        img = tf.io.read_file(file_path)
        img = decode_img(img)
        return img, label

    labeled_ds = list_ds.map(process_path, num_parallel_calls=AUTOTUNE)
    if take_size is None:
        return labeled_ds.shuffle(shuffle_buffer_size).padded_batch(
            batch_size=batch_size
        )
    else:
        train_labeled_ds = (
            list_ds.map(process_path, num_parallel_calls=AUTOTUNE)
            .skip(take_size)
            .shuffle(shuffle_buffer_size)
            .padded_batch(batch_size=batch_size)
        )
        test_labeled_ds = (
            list_ds.map(process_path, num_parallel_calls=AUTOTUNE)
            .take(take_size)
            .padded_batch(batch_size=batch_size)
        )
        return train_labeled_ds, test_labeled_ds


def images_dir(
    path,
    hasTest=False,
    img_height=224,
    img_width=224,
    batch_size=64,
    shuffle_buffer_size=3000,
    take_size=None,
):
    path = (work_path + path).replace("//", "/")
    if hasTest:
        train_dataset = images_dir_basis_function(
            path=path + "/train",
            img_height=img_height,
            img_width=img_width,
            batch_size=batch_size,
            shuffle_buffer_size=3000,
            take_size=None,
        )
        test_dataset = images_dir_basis_function(
            path=path + "/test",
            img_height=img_height,
            img_width=img_width,
            batch_size=batch_size,
            shuffle_buffer_size=3000,
            take_size=None,
        )
        return train_dataset, test_dataset
    else:
        return images_dir_basis_function(
            path=path,
            img_height=img_height,
            img_width=img_width,
            batch_size=batch_size,
            shuffle_buffer_size=shuffle_buffer_size,
            take_size=take_size,
        )


def text_dir_basis_function(
    one_hot_label=True,
    shuffle_buffer_size=50000,
    batch_size=64,
    take_size=None,
    path=None,
):
    import tensorflow_datasets as tfds

    FILE_NAMES = os.listdir(path)
    labeled_data_sets = []

    def labeler(example, index):
        return example, tf.cast(index, tf.int64)

    for i, file_name in enumerate(FILE_NAMES):
        lines_dataset = tf.data.TextLineDataset(os.path.join(path, file_name))
        labeled_dataset = lines_dataset.map(lambda ex: labeler(ex, i))
        labeled_data_sets.append(labeled_dataset)

    all_labeled_data = labeled_data_sets[0]
    for labeled_dataset in labeled_data_sets[1:]:
        all_labeled_data = all_labeled_data.concatenate(labeled_dataset)

    all_labeled_data = all_labeled_data.shuffle(
        shuffle_buffer_size, reshuffle_each_iteration=False
    )

    tokenizer = tfds.features.text.Tokenizer()

    vocabulary_set = set()
    for text_tensor, _ in all_labeled_data:
        some_tokens = tokenizer.tokenize(text_tensor.numpy())
        vocabulary_set.update(some_tokens)

    encoder = tfds.features.text.TokenTextEncoder(vocabulary_set)

    def encode(text_tensor, label):
        encoded_text = encoder.encode(text_tensor.numpy())
        return encoded_text, label

    def encode_map_fn(text, label):
        encoded_text, label = tf.py_function(
            encode, inp=[text, label], Tout=(tf.int64, tf.int64)
        )

        encoded_text.set_shape([None])
        label.set_shape([])

        return encoded_text, label

    def map_one_hot_func(images, label):
        label = tf.one_hot(label, depth=3)
        return images, label

    all_encoded_data = all_labeled_data.map(encode_map_fn)
    if one_hot_label:
        all_encoded_data = all_labeled_data.map(map_one_hot_func)

    if take_size is None:
        train_data = all_encoded_data.shuffle(
            shuffle_buffer_size).padded_batch(batch_size)
        return train_data
    else:
        train_data = all_encoded_data.skip(
            take_size).shuffle(shuffle_buffer_size)
        train_data = train_data.padded_batch(batch_size)

        test_data = all_encoded_data.take(take_size).padded_batch(batch_size)

        return train_data, test_data


def text_dir(
    path=None,
    has_test=False,
    one_hot_label=True,
    shuffle_buffer_size=50000,
    batch_size=64,
    take_size=None,
):
    path = (work_path + path).replace("//", "/")
    if has_test:
        train_dataset = text_dir_basis_function(
            path=path + "/train",
            one_hot_label=one_hot_label,
            shuffle_buffer_size=shuffle_buffer_size,
            batch_size=batch_size,
        )
        test_dataset = text_dir_basis_function(
            path=path + "/test",
            one_hot_label=one_hot_label,
            shuffle_buffer_size=shuffle_buffer_size,
            batch_size=batch_size,
        )
        return train_dataset, test_dataset
    else:
        return text_dir_basis_function(
            path=path,
            one_hot_label=one_hot_label,
            shuffle_buffer_size=shuffle_buffer_size,
            batch_size=batch_size,
            take_size=take_size,
        )


def numpy_reader(path, batch_size=64, shuffle_buffer_size=1000):
    path = (work_path + path).replace("//", "/")
    with np.load(path) as data:
        train_examples = data["x_train"]
        train_labels = data["y_train"]
        test_examples = data["x_test"]
        test_labels = data["y_test"]

    train_dataset = tf.data.Dataset.from_tensor_slices(
        (train_examples, train_labels))
    test_dataset = tf.data.Dataset.from_tensor_slices(
        (test_examples, test_labels))

    train_dataset = train_dataset.shuffle(
        shuffle_buffer_size).batch(batch_size)
    test_dataset = test_dataset.batch(batch_size)

    return train_dataset, train_labels, test_dataset, test_labels


def csv_pandas_dir(
    path,
    has_test=None,
    labels=None,
    batch_size=128,
    shuffle_buffer_size=3000,
    take_size=None,
):
    path = (work_path + path).replace("//", "/")
    import pandas as pd

    df = pd.read_csv(path + "train.csv")
    y_df = df.pop(labels)

    if has_test:
        x_test_df = pd.read_csv(work_path + path + "test.csv")
        y_test_df = x_test_df.pop(labels)
        train_dataset = (
            tf.data.Dataset.from_tensor_slices((df.values, y_df.values))
            .shuffle(shuffle_buffer_size)
            .batch(batch_size)
        )
        if take_size is None:
            return train_dataset
        test_dataset = tf.data.Dataset.from_tensor_slices(
            (x_test_df.values, y_test_df.values)
        ).batch(batch_size)

        return train_dataset, test_dataset
    else:
        train_dataset = (
            tf.data.Dataset.from_tensor_slices((df.values, y_df.values))
            .skip(take_size)
            .shuffle(shuffle_buffer_size)
            .batch(batch_size)
        )
        test_dataset = (
            tf.data.Dataset.from_tensor_slices((df.values, y_df.values))
            .take(take_size)
            .batch(batch_size)
        )

        return train_dataset, test_dataset
