# encoding: utf-8
import autokeras as ak
from DataReader.TFDS import images_dir

train_dataset = images_dir(
    path="/",
    shuffle_buffer_size=1,
    hasTest=True,
    img_height=1,
    img_width=1,
    batch_size=1,
    take_size=1,
)
model = ak.TextClassifier(
    loss="hinge", metrics=["poisson"], max_trials=2, overwrite=True, seed=2
)
model.fit(train_dataset, validation_split=0.3, epochs=1)
evaluate = model.evaluate(train_dataset)
model_save = model.export_model()
model_save.save("./", save_format="tf")
