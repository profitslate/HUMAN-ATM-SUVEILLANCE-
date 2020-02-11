"""
This file is responsible for controlling door open feature
And for door close you can check door_close file
This mechanism will not work now but we will work on this mechanism in future version
"""

isOpened = True


def open_door():
    global isOpened
    print("Door is open now :: open_door()")
    isOpened = True

