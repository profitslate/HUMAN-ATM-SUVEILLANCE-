"""
Using ImageAi and our custom helmet detection yoloV3 model
we are going to detect helmet in the face of human
"""

from imageai.Detection.Custom import CustomObjectDetection
import cv2


def threat_detection():
    detect = CustomObjectDetection()
    detect.setModelTypeAsYOLOv3()
    detect.setModelPath("data/model/detection_model-ex-063--loss-0009.921.h5")
    detect.setJsonPath("data/json/detection_config.json")
    detect.loadModel()

    URL = ""
    video_capture = cv2.VideoCapture(URL)
    frame = video_capture.read()
    cv2.imwrite("image/image.jpg", frame)
    detections = detect.detectObjectsFromImage(input_image="image/image.jpg", output_image_path="image/imageNew.jpg",
                                               minimum_percentage_probability=55)
    if len(detections) > 0:
        print("detected")
        return True

    else:
        print("safe But need to look over :: final_threat_detector()")
        return False

# #referencing current directory
# dir = os.getcwd()
#
# #setting model path and jason path for the yoloV3 mdoel
# model_path = "data_for_yolov3/models/detection_model-ex-001--loss-0505.127.h5"
# json_path = "data_for_yolov3/json/detection_config.json"
#
# king = CustomObjectDetection()
# king.setModelTypeAsYOLOv3()
# king.setModelPath(model_path)
# king.setJsonPath(json_path)
# king.loadModel()
#
# #detections = king.detectObjectsFromImage(input_image="image.jpg", output_image_path= "imageNew.jpg",
# minimum_percentage_probability=55) #detections = king.detectObjectsFromImage(
# input_image="data_for_yolov3/train/images/img_50.jpg", output_image_path= "imageNewWithHelmet.jpg",
# minimum_percentage_probability=55) detections = king.detectObjectsFromImage(input_image="imageWithHelmet.jpg",
# output_image_path= "imageNewWithHelmet.jpg", minimum_percentage_probability=55)
#
# print(detections)
# for eachDetection in detections:
#     if eachDetection["name"] == "helmet" :
#         print ("please open your helmet")
#         print ("------------------------")
