# -*- coding:utf-8 -*-
from keras import models
from keras import layers
from keras import Input


# 利用训练后的Word2vec自定义Embedding的训练矩阵 每行代表一个词(结合独热编码和矩阵乘法理解)
# 卷积+BN+激活函数
def conv_block(x, filter1, kernel):
    # 卷积
    x = layers.Conv1D(filter1, kernel, padding='same', use_bias=False)(x)
    # 标准化
    x = layers.BatchNormalization()(x)
    # 激活函数，使用relu激活函数，保证移动端的精度
    x = layers.Activation('relu')(x)

    return x


def net101(input_shape):
    """

    Parameters
    ----------
    input_shape

    Returns
    -------

    """
    # 训练模型
    main_input = Input(shape=(100,), dtype='float64')

    input_shape = input_shape
    x = layers.Embedding(len(vocab) + 1, 100, input_length=100)(input_shape)

    # 在形式参数中传入模型需要的参数
    # input_dim, output_dim, input_length

    x = conv_block(x, 32, 1)

    x = layers.MaxPool1D(100 - 5, 3, padding='same')(x)

    x = conv_block(x, 64, 1)
    x = conv_block(x, 64, 1)

    x = conv_block(x, 128, 1)
    x = conv_block(x, 256, 1)

    x = layers.Flatten()(x)

    x = layers.Dropout(0.3)(x)

    x = layers.Dense(256, activation='relu')(x)
    x = layers.Dropout(0.2)(x)
    x = layers.Dense(units=14, activation='softmax')(x)

    model = models.Model(inputs=main_input, outputs=x)

    return model
