# import face_recognition
import cv2
import numpy as np
import os
import pynput


def load_face_images() -> list:
    ...


def get_num_of_images() -> int:
    count = 0
    directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")

    for path in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, path)):
            count += 1

    return count - 1


def save_face_images() -> None:
    camera = cv2.VideoCapture(1)
    name_of_img = get_num_of_images()

    while True:
        ret, frame = camera.read()

        cv2.imshow("Frame", frame)

        if cv2.waitKey(1) == ord("s"):
            cv2.imwrite(f"images/{name_of_img}.jpg", frame)
            name_of_img = int(name_of_img) + 1
            name_of_img = str(name_of_img)

        if cv2.waitKey(1) == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()


save_face_images()
