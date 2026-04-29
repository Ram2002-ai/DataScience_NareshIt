# import ultralytics
# ultralytics.checks()

# from ultralytics import YOLO
# model = YOLO('yolov8n.pt')

# # detection_output=model.predict(source=r"E:\Photos\horse.jpg", save=True)
# detection_output=model.predict(source=r"https://media.wired.com/photos/5eceec5684d586f61b4d6abb/master/pass/Transpo-AddisAbabastreet-464372138.jpg", save=True)

# print(detection_output)


from ultralytics import YOLO

# Load a COCO-pretrained YOLO26n model
model = YOLO("yolo26n.pt")

# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(data="coco8.yaml", epochs=100, imgsz=640,  save=True)

# Run inference with the YOLO26n model on the 'bus.jpg' image
results = model("path/to/bus.jpg", save=True)