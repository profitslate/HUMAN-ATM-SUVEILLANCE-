"""
THis file is responsible for door close mechanism
This mechanism will not work now but we will work on this mechanism in future version
For open door you can find a open_door file
"""

import open_door
import report


def close_door():
    print("Doors are locked until he will remove his helmet :: close_doors()")
    open_door.isOpened = False


def lock_door():
    print("The is permanently Locked ::: ")
    report.report()
    open_door.isOpened = False
