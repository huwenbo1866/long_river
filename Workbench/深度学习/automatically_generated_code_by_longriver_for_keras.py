# encoding: utf-8
import tensorflow as tf
import tensorflow.keras as keras
from tensorflow.keras.activations import *
from DataReader.TFDS import images_dir

train_dataset = images_dir(
    path="/", hasTest=True, img_height=1, img_width=1, batch_size=1
)
strategy = tf.distribute.MirroredStrategy()
with strategy.scope():
    model = keras.Sequential()
    model.compile(
        optimizer=keras.optimizers.SGD(),
        loss=keras.losses.Poisson(),
        metrics=[
            "mean_absolute_error",
        ],
    )
tbCallBack = keras.callbacks.TensorBoard(
    log_dir="1", write_graph=True, write_grads=True, write_images=True
)
model.fit_generator(
    train_dataset,
    batch_size=1,
    epochs=1,
    steps_per_epoch=1,
    shuffle=True,
    callbacks=[tbCallBack],
)
evaluate_loss, evaluate_mean_absolute_error = model.evaluate(
    train_dataset,
    batch_size=1,
)
model.save("./name.h5")
