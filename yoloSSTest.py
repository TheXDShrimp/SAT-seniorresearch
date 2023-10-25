from ultralytics import YOLO

# Load a COCO-pretrained YOLOv3n model
model = YOLO('yolov8n.pt')


# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(data='coco128.yaml', epochs=3, imgsz=640)

# Run inference with the YOLOv3n model on the 'bus.jpg' image
results = model('path/to/bus.jpg')
