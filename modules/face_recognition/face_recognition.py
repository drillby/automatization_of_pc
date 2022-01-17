from webbrowser import get
import cv2
import numpy as np
import os
import random
from matplotlib import pyplot as plt
from errors import custom_errors as custom_errs

from tensorflow.keras.models import Model
from tensorflow.keras.layers import Layer, Conv2D, Dense, MaxPooling2D, Input, Flatten
from tensorflow.keras.metrics import Precision, Recall
import tensorflow as tf


class L1Dist(Layer):
    def __init__(self, **kwargs):
        super().__init__()

    def call(self, input_embedding, validation_embedding):
        return tf.math.abs(input_embedding - validation_embedding)


def save_face_images() -> None:
    """Will start webcam and save face images when you press 'a' or 'p'.
    Will quit on 'q' pressed.

    Raises:
        cus_err.CameraError: Raised when unable to open camera.
        cus_err.FrameError: Raised when unable to process frame from webcam.
    """
    import uuid

    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        raise custom_errs.CameraError("Unable to open camera")

    while True:
        ret, frame = camera.read()
        frame = frame[
            120 : 120 + 250, 200 : 200 + 250, :
        ]  # cut frame to 250x250 pixels

        if not ret:
            raise custom_errs.FrameError("Cannot recieve frame")

        # Anchor collection
        if cv2.waitKey(1) == ord("a"):
            img_name = os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                "data",
                "anchor",
                f"{uuid.uuid1()}.jpg",
            )
            cv2.imwrite(img_name, frame)

        # Positive collection
        if cv2.waitKey(1) == ord("p"):
            img_name = os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                "data",
                "positive",
                f"{uuid.uuid1()}.jpg",
            )
            cv2.imwrite(img_name, frame)

        cv2.imshow("Frame", frame)

        if cv2.waitKey(1) == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()

    return


def preprocess_images(file_path) -> list:
    """Will preprocess images(decode, resize and mapping)

    Args:
        file_path (path): Path to an image

    Returns:
        tf.python.framework.ops.EagerTensor: Array like object representing image.
    """
    byte_img = tf.io.read_file(file_path)
    img = tf.io.decode_jpeg(byte_img)
    img = tf.image.resize(img, (100, 100))
    img = img / 250.0

    return img


def preprocess_twin(input_img, validation_img, label):
    return preprocess_images(input_img), preprocess_images(validation_img), label


def make_embedding():
    inp = Input(shape=(100, 100, 3), name="input_img")

    c1 = Conv2D(64, (10, 10), activation="relu")(inp)
    m1 = MaxPooling2D(64, (2, 2), padding="same")(c1)

    c2 = Conv2D(128, (7, 7), activation="relu")(m1)
    m2 = MaxPooling2D(64, (2, 2), padding="same")(c2)

    c3 = Conv2D(128, (4, 4), activation="relu")(m2)
    m3 = MaxPooling2D(64, (2, 2), padding="same")(c3)

    c4 = Conv2D(256, (4, 4), activation="relu")(m3)
    f1 = Flatten()(c4)
    d1 = Dense(4096, activation="sigmoid")(f1)

    return Model(inputs=[inp], outputs=[d1], name="embedding")


def make_siamese_model():
    input_image = Input(name="input_img", shape=(100, 100, 3))

    validation_image = Input(name="validation_img", shape=(100, 100, 3))

    siamese_layer = L1Dist()
    siamese_layer._name = "distance"
    distances = siamese_layer(embedding(input_image), embedding(validation_image))

    classifier = Dense(1, activation="sigmoid")(distances)

    return Model(
        inputs=[input_image, validation_image],
        outputs=classifier,
        name="SiameseNetwork",
    )


def disable_gpu() -> None:
    """
    Will run TF on CPU.
    Don't run this unless your GPU doesn't support CUDA
    """
    os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

    if tf.test.gpu_device_name():
        print("GPU found")
    else:
        print("GPU disabled")

    return


@tf.function
def train_step(batch):

    # Record all of our operations
    with tf.GradientTape() as tape:
        # Get anchor and positive/negative image
        X = batch[:2]
        # Get label
        y = batch[2]

        # Forward pass
        yhat = siamese_model(X, training=True)
        # Calculate loss
        loss = binary_cross_loss(y, yhat)
    print(loss)

    # Calculate gradients
    grad = tape.gradient(loss, siamese_model.trainable_variables)

    # Calculate updated weights and apply to siamese model
    opt.apply_gradients(zip(grad, siamese_model.trainable_variables))

    # Return loss
    return loss


def train(data, EPOCHS):
    # Loop through epochs
    for epoch in range(1, EPOCHS + 1):
        print(f"\n Epoch {epoch}/{EPOCHS}")
        progbar = tf.keras.utils.Progbar(len(data))

        # Loop through each batch
        for idx, batch in enumerate(data):
            # Run train step here
            train_step(batch)
            progbar.update(idx + 1)

        # Save checkpoints
        if epoch % 10 == 0:
            checkpoint.save(file_prefix=checkpoint_prefix)


disable_gpu()


anchor = tf.data.Dataset.list_files(
    os.path.join(os.path.dirname(os.path.realpath(__file__)), "data", "anchor")
    + "\*.jpg"
).take(300)
positive = tf.data.Dataset.list_files(
    os.path.join(os.path.dirname(os.path.realpath(__file__)), "data", "positive")
    + "\*.jpg"
).take(300)
negative = tf.data.Dataset.list_files(
    os.path.join(os.path.dirname(os.path.realpath(__file__)), "data", "negative")
    + "\*.jpg"
).take(300)


positives = tf.data.Dataset.zip(
    (anchor, positive, tf.data.Dataset.from_tensor_slices(tf.ones(len(anchor))))
)
negatives = tf.data.Dataset.zip(
    (anchor, negative, tf.data.Dataset.from_tensor_slices(tf.zeros(len(anchor))))
)
data = positives.concatenate(negatives)


data = data.map(preprocess_twin)
data = data.cache()
data = data.shuffle(buffer_size=1024)
# Created dataset to learn from

train_data = data.take(round(len(data) * 0.7))
train_data = train_data.batch(16)
train_data = train_data.prefetch(8)

test_data = data.skip(round(len(data) * 0.7))
test_data = test_data.take(round(len(data) * 0.3))
test_data = test_data.batch(16)

embedding = make_embedding()

siamese_model = make_siamese_model()

binary_cross_loss = tf.losses.BinaryCrossentropy()
opt = tf.keras.optimizers.Adam(1e-4)

checkpoint_dir = "./training_checkpoints"
checkpoint_prefix = os.path.join(checkpoint_dir, "ckpt")
checkpoint = tf.train.Checkpoint(opt=opt, siamese_model=siamese_model)

EPOCHS = 50
train(train_data, EPOCHS)

test_input, test_val, y_true = test_data.as_numpy_iterator().next()
y_hat = siamese_model.predict([test_input, test_val])
# Post processing the results
prediction_results = [1 if prediction > 0.5 else 0 for prediction in y_hat]
zeros = 0
ones = 0
for i in range(len(prediction_results)):
    if prediction_results[i] == 1:
        ones += 1
    else:
        zeros += 1

print(f"Number of predictions: {ones+zeros}")
print(f"Number of successful predictions: {ones}")
print(f"Number of unsuccessful predictions: {zeros}")

save = input("Save build?[y/n]: ")
if save == "y":
    siamese_model.save("siamesemodelv2.h5")
