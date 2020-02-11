import cv2
import face_recognition
import open_door
import close_doors
import threading
import report


def threat_remover(human_count):
    close_doors.lock_door()
    print("it will continue until threat will not removed")
    URL=""
    video_capture = cv2.VideoCapture(URL)
    while True:
        ret, frame = video_capture.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(frame)

        if 3 > human_count == len(face_locations) > 0:
            print("All safe You can Proceed now")
            open_door.open_door()

        elif 3 < human_count > len(face_locations) > 0:
            print("Everyone have to remove there face cover")
            print("You have more 10 Secs")
            timer = threading.Timer(10)
            timer.start()
            report.report()

        elif human_count < len(face_locations) > 0:
            print("We information send to the nearest sources you have to wait until they come")
            report.report()
