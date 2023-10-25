from ultralytics import YOLO
from ultralytics.yolo.v8.detect.predict import DetectionPredictor
import cv2
import numpy as np
import pandas as pd

model = YOLO("yolov8s.pt")

# predict on cars.jpg and display it

results = model("cars.jpg")
print()
print(results[0].boxes.xyxy[0])
print()



# # Create a pandas dataframe.
# df = pd.DataFrame()

# # Add the yolo output data to the pandas dataframe.
# for i in range(len(results)):
#   df = df.append({'x': results[i, 0], 'y': results[i, 1], 'w': results[i, 2], 'h': results[i, 3]}, ignore_index=True)








CLASS_LABELS = {2: "car", 67: "cell phone"}

class BoundBox:
    def __init__(self, xmin, ymin, height, width, confidence=None, class_id=None, class_label=None):
        self.xmin = xmin
        self.ymin = ymin
        self.height = height
        self.width = width
        self.confidence = confidence
        self.class_id = class_id
        self.class_label = class_label

    def get_label(self):
        return self.class_label

    def get_confidence(self):
        return self.confidence

    def get_coordinates(self):
        return (self.xmin, self.ymin, self.xmax, self.ymax)

    def __repr__(self):
        return "({:.2f}, {:.2f}, {:.2f}, {:.2f}: {})".format(self.xmin, self.ymin, self.xmin + self.width, self.ymin + self.height, self.class_label)

def parse_yolo_output(yolo_output, class_labels: dict=CLASS_LABELS):
    results = []
    for item in yolo_output:
        x, y, width, height, confidence, class_id = item
        
        if class_id not in class_labels:
            continue

        # Create a dictionary for each detected object
        detection = {
            "x": x,
            "y": y,
            "width": width,
            "height": height,
            "confidence": confidence,
            "class_id": class_id,
            "class_label": class_labels[class_id]
        }
        results.append(detection)

    return results

print(parse_yolo_output(results[0]))




# lst = []
# cap = cv2.VideoCapture(0)
# while cap.isOpened():
#     ret, frame = cap.read()
    
#     # Make detections
#     results = model(frame)
#     cv2.imshow('YOLO', np.squeeze(results.render())) 
    
#     df = results.pandas().xyxy[0]
    
#     for i in df['name']: # name->labels
#         lst.append(i)
    
    
#     if cv2.waitKey(10) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()