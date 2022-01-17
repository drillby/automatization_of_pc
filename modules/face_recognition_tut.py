import cv2
import numpy as np
import os
import random
from matplotlib import pyplot as plt
import errors.custom_errors as custome_err

from tensorflow.keras.models import Model
from tensorflow.keras.layers import Layer, Conv2D, Dense, MaxPooling2D, Input, Flatten
import tensorflow as tf

def limit_gpu_memory():
    """
    Avoid OOM errors by setting GPU memory consumption growth
    Only nessecary if you are using PC with GPU
    """
    gpus = tf.config.experimental.list_physical_devices('GPU')
    for gpu in gpus:
        tf.config.experimental.set_memory_growth(gpu, True)
    return

def get_num_of_images() -> int:
    """Will return the number of images in the images folder.
    Necessary for correct naming of images.

    Returns:
        int: Number of images
    """
    count = 0
    directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")

    for path in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, path)):
            count += 1

    return count - 1

def save_face_images() -> None:
    """Will start webcam and save face images when you press 's'.
    Will quit on 'q' pressed.

    Raises:
        cus_err.CameraError: Raised when unable to open camera.
        cus_err.FrameError: Raised when unable to process frame from webcam.
    """

    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        raise custome_err.CameraError("Unable to open camera")
    name_of_img = get_num_of_images()
    directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")

    while True:
        ret, frame = camera.read()

        if not ret:
            raise custome_err.FrameError("Cannot recieve frame")

        cv2.imshow("Frame", frame)

        if cv2.waitKey(1) == ord("s"):
            cv2.imwrite(f"{directory}/{name_of_img}.jpg", frame)
            name_of_img = int(name_of_img) + 1
            name_of_img = str(name_of_img)

        if cv2.waitKey(1) == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()

    return

limit_gpu_memory()