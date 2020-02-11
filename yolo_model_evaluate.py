from imageai.Detection.Custom import DetectionModelTrainer

trainer = DetectionModelTrainer()
trainer.setModelTypeAsYOLOv3()
trainer.setDataDirectory(data_directory="data_for_yolov3")
metrics = trainer.evaluateModel(model_path="data_for_yolov3/models", json_path="data_for_yolov3/json/detection_config.json", iou_threshold=0.5, object_threshold=0.3, nms_threshold=0.5)