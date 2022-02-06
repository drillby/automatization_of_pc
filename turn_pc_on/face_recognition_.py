import face_recognition
import cv2
import numpy as np

# This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
# other example, but it includes some basic performance tweaks to make things run a lot faster:
#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Get a reference to webcam #0 (the default one)


def common_data(list1: list, list2: list) -> bool:
    """Will check if list1 and list2 contain the same number of same elements

    Args:
        list1 (list): List to compare
        list2 (list): List to compare

    Returns:
        bool: True=common data, False=not common data
    """
    for x in list1:
        for y in list2:
            if x == y:
                return True

    else:
        return False


MAC = "fc:aa:14:03:e6:37"
BRODCAST_IP = "192.168.132.255"


def recognize():
    video_capture = cv2.VideoCapture(0)

    # Load a sample picture and learn how to recognize it.
    face_1 = face_recognition.load_image_file("images/face_1.jpg")
    face_2 = face_recognition.load_image_file("images/face_2.jpg")
    face_3 = face_recognition.load_image_file("images/face_3.jpg")

    face_encoding_1 = face_recognition.face_encodings(face_1)[0]
    face_encoding_2 = face_recognition.face_encodings(face_2)[0]
    face_encoding_3 = face_recognition.face_encodings(face_3)[0]

    # Create arrays of known face encodings and their names
    known_face_encodings = [face_encoding_1, face_encoding_2, face_encoding_3]
    known_face_names = [
        "Pavel Podrazky",
        "Pavel Podrazky",
        "Pavel Podrazky"
    ]

    # Initialize some variables
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    while True:
        # Grab a single frame of video
        ret, frame = video_capture.read()

        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Only process every other frame of video to save time
        if process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(
                rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(
                    known_face_encodings, face_encoding)
                name = "Unknown"

                # # If a match was found in known_face_encodings, just use the first one.
                # if True in matches:
                #     first_match_index = matches.index(True)
                #     name = known_face_names[first_match_index]

                # Or instead, use the known face with the smallest distance to the new face
                face_distances = face_recognition.face_distance(
                    known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]

                face_names.append(name)

        process_this_frame = not process_this_frame

        # Display the results
        if common_data(face_names, known_face_names):
            return True

        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release handle to the webcam
    video_capture.release()
    cv2.destroyAllWindows()
