"""
This hole file to ensure proper human entered in the atm.

In india there are so many atm out there where you can't find any security gourd
and this is really peak point for those people who are thread to the society.

This system is basically for those kind of atm's where companies are not able to
invest for a security gourd to give it a bit  more security

In this project we use 'face_recognition' a simple and one of those libraries for face recognition
and cv2 most popular image processing library

THis is totally on beta mode so more accuracy and more ... feature will come through the time
"""

import human_detection
import face_detection
import threat_detection
import threat_remover
import open_door
import close_doors

transaction_status = False
retry = 0
recheck = 0
face_checking_trying = 0

"""
Face Checking function
Here our system check for number of human and number of face are same or not....
"""


def face_checking(human_counts):
    global face_checking_trying
    face_counts = face_detection.count_faces()
    if compare(human_counts, face_counts):
        return True
    else:
        print("Something wrong inform them to remove mask if they have any ::::")
        if face_checking_trying < 6:
            face_checking(human_counts)
        else:
            close_doors.lock_door()


def compare(a, b):
    if a == b:
        return True
    else:
        return False


def enter_or_not():
    if open_door.isOpened:
        atm_main()
    else:
        print("Machine In power Save mode")


"""
This is atm main function where main algorithms and conditions are working
"""


def atm_main():
    global retry, recheck
    human_counts = human_detection.count_human()

    if human_counts == 0:
        print("tend to recheck :::: ")
        retry += 1
        if retry < 6:
            atm_main()
        else:
            close_doors.lock_door()
    else:
        if 0 < human_counts > 3:
            print("Everything is working fine ::: In human checking ")
            if face_checking(human_counts):
                print("Everything Working Fine")
                safe = True
                if safe and recheck == 6:
                    print("Final checking end everything working fine")
                elif recheck < 6:
                    recheck += 1
                    atm_main()
                else:
                    print("May be threat is there")
                    close_doors.lock_door()
            else:
                if threat_detection.threat_detection():
                    threat_remover.threat_remover(human_counts)
        else:
            print("Only two people are allowed")
            retry = 0
            atm_main()


'''
It work kind a main function 
It's as if the interpreter inserts this at the top
of your module when run as the main program.
'''
if __name__ == "__main__":
    enter_or_not()
