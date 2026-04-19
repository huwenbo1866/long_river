# encoding: utf-8
import tensorflow as tf
import tensorflow.keras as keras
from DataReader.TFDS import images_dir
from tensorflow.keras.applications.resnet50 import ResNet50

train_dataset = images_dir(
    path="/",
    hasTest=True,
    shuffle_buffer_size=1,
    img_height=1,
    img_width=1,
    batch_size=1,
    take_size=1,
)
strategy = tf.distribute.MirroredStrategy()
with strategy.scope():
    model = ResNet50(weights=None, input_shape=(1, 2), classes=2)
    model.compile(
        optimizer=keras.optimizers.Adam(
            epsilon=1,
            amsgrad=True,
            beta2=2,
            beta1=1,
            learning_rate=1,
        ),
        loss=keras.losses.CosineSimilarity(),
        metrics=[
            "categorical_crossentropy",
        ],
    )
model.fit(
    train_dataset,
    batch_size=1,
    epochs=1,
    steps_per_epoch=1,
    validation_split=0.2,
    shuffle=True,
)
evaluate_loss, evaluate_categorical_crossentropy = model.evaluate(
    train_dataset,
    batch_size=2,
)
model.save("./name/name.h5")
