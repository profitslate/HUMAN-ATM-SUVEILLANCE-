"""
importing Model trainer component which you can find in imageai library

ImageAi is a python library which uses tensorflow deep learning framework
It contain proper functions to detect object from images, videos,
and also build custom models as per our need.....
"""
from imageai.Detection.Custom import DetectionModelTrainer

# creating Object of DetectionModelTrainer()
trainer = DetectionModelTrainer()

# Set model as yolov3 which is a COCO model
trainer.setModelTypeAsYOLOv3()

# setting the directory location where my reference images are present
trainer.setDataDirectory(data_directory="data_for_yolov3")

# method to start the training
trainer.setTrainConfig(object_names_array=["helmet"], batch_size=8, num_experiments=100)
trainer.trainModel()
