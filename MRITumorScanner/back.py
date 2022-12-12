import numpy as np
import tensorflow as tf
import keras


# Triggered once in runner in order to create and train the model, then commented out.
def model_creating():
    # Loading images as a training dataset from my image directory
    train_ds = tf.keras.utils.image_dataset_from_directory(
        '../data/training',
        validation_split=0.2,
        subset="training",
        seed=123,
        image_size=(512, 512),
        batch_size=32)

    # Loading validation dataset from image directory
    val_ds = tf.keras.utils.image_dataset_from_directory(
        '../data/testing',
        validation_split=0.2,
        subset="validation",
        seed=123,
        image_size=(512, 512),
        batch_size=32)

    # Getting class names and fixing noises
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

    # Fitting the model, will do more epochs if the size of dataset will allow to.
    epochs = 1
    model.fit(
        train_ds,
        validation_data=val_ds,
        epochs=epochs
    )

    # Saving the model
    model.save('BrainModel')


# Loading my pretrained model for re-use,
# triggered by Analyze button in GUI.
def use_model(path):
    # Loading model
    model = keras.models.load_model("BrainModel")
    # Using the picture loaded by user
    img = tf.keras.utils.load_img(
        path, target_size=(512, 512)
    )
    # Turning the image to array
    img_array = tf.keras.utils.img_to_array(img)
    # Create a batch
    img_array = tf.expand_dims(img_array, 0)
    # Getting result and confidence level
    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])
    class_names = ['Glioma', 'Meningioma', 'no known tumor', 'Pituitary']
    # Returning the result to the GUI
    return [class_names[np.argmax(score)], 100 * np.max(score)]
