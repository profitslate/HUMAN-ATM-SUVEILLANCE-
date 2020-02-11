"""
This file basically concentrate on face detection system
it also contail a second method name thread remover which basically final stage for our system for now
"""

import cv2
import face_recognition
import threading
import open_door as od
import report as rta

threat_or_not = False


def count_faces():
    URL = ""
    video_capture = cv2.VideoCapture(URL)
    ret, frame = video_capture.read()

    # Converting BGR to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # face_location is an array where we are collection face location axis in every frame.
    face_locations = face_recognition.face_locations(frame)
    video_capture.release()
    return len(face_locations)


'''
This is final stage of the security when something wrong noticed
It will continue until the thread will not removed
And it is responsible to report to the authority
'''


def threat_remover(video_capture, human_count):
    print("it will continue until threat will not removed")

    while True:
        ret, frame = video_capture.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(frame)

        if 3 > human_count == len(face_locations) > 0:
            print("All safe You can Proceed now")
            od.open_door()

        elif 3 < human_count > len(face_locations) > 0:
            print("Everyone have to remove there face cover")
            print("You have more 10 Secs")
            timer = threading.Timer(10)
            timer.start()
            rta.report()

        elif human_count < len(face_locations) > 0:
            print("We information send to the nearest sources you have to wait until they come")
            rta.report()
