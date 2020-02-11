"""
At the first when someone will enter into the atm this mechanism will keep checking for human
It will check until it will not find a human entered in the system for a certain time
"""

import cv2

'''
hog representing cv2.HOGDescriptor()
'''
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


def count_human():
    URL = ""
    video_capture = cv2.VideoCapture(URL)
    frame = video_capture.read()

    # converting frame to BGR format to GRAY format
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    boxes, humans = hog.detectMultiScale(gray_frame, winStride=(8, 8))
    video_capture.release()
    return len(humans)

