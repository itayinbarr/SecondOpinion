import matplotlib.pyplot as plt
import numpy as np
import os
import PIL
import tensorflow as tf
import matplotlib.pyplot as plt
import keras
from PIL import Image

# Used once in runner, then commented out
from numpy import asarray


def model_creating():
    # Loading training dataset from image directory
    train_ds = tf.keras.utils.image_dataset_from_directory(
        '../data/training',
        validation_split=0.2,
        subset="training",
        seed=123,
        image_size=(512, 512),
        batch_size=32)

    # Loading val dataset from image directory
    val_ds = tf.keras.utils.image_dataset_from_directory(
        '../data/testing',
        validation_split=0.2,
        subset="validation",
        seed=123,
        image_size=(512, 512),
        batch_size=32)

    class_names = train_ds.class_names
    AUTOTUNE = tf.data.AUTOTUNE
    train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
    val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)

    # Creating the model
    num_classes = len(class_names)
    model = keras.Sequential([
        keras.layers.Rescaling(1. / 255, input_shape=(512, 512, 3)),
        keras.layers.Conv2D(16, 3, padding='same', activation='relu'),
        keras.layers.MaxPooling2D(),
        keras.layers.Conv2D(32, 3, padding='same', activation='relu'),
        keras.layers.MaxPooling2D(),
        keras.layers.Conv2D(64, 3, padding='same', activation='relu'),
        keras.layers.MaxPooling2D(),
        keras.layers.Flatten(),
        keras.layers.Dense(128, activation='relu'),
        keras.layers.Dense(num_classes)
    ])

    # Compiling the model
    model.compile(optimizer='adam',
                  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                  metrics=['accuracy'])

    # Fitting the model
    epochs = 1
    model.fit(
        train_ds,
        validation_data=val_ds,
        epochs=epochs
    )

    # Saving the model
    model.save('BrainModel')
    predictions = model.predict(val_ds)
    print(class_names[np.argmax(predictions[0])])


# Loading the pretrained model for you own use
def use_model(path):
    model = keras.models.load_model("BrainModel")
    img = tf.keras.utils.load_img(
        path, target_size=(512, 512)
    )
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create a batch

    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])
    class_names = ['Glioma', 'Meningioma', 'no known tumor', 'Pituitary']
    return [class_names[np.argmax(score)], 100 * np.max(score)]
