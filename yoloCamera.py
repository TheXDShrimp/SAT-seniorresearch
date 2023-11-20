# Initialize Global Variables
CLASS_LABELS = {0: "person", 2: "car", 39: "bottle", 67: "cell phone"}

from ultralytics import YOLO

model = YOLO("yolov8n.pt")



# predict on image
model_result = model("cars.jpg")



class BoundBox:
    def __init__(self, xmin, ymin, height, width, confidence=None, class_id=None, class_label=None):
        self.xmin = xmin
        self.ymin = ymin
        self.height = height
        self.width = width
        self.confidence = confidence
        self.class_id = class_id
        self.class_label = class_label
        
    def __init__(self, dic: dict):
        self.xmin = dic["x"]
        self.ymin = dic["y"]
        self.height = dic["h"]
        self.width = dic["w"]
        self.confidence = dic["confidence"]
        self.class_id = dic["class"]
        self.class_label = CLASS_LABELS[self.class_id] if self.class_id in CLASS_LABELS else None

    def get_label(self):
        return self.class_label

    def get_confidence(self):
        return self.confidence

    def get_coordinates(self):
        return (self.xmin, self.ymin, self.xmin + self.width, self.ymin + self.height)

    def __repr__(self):
        return "({:.2f}, {:.2f}, {:.2f}, {:.2f}: {})".format(self.xmin, self.ymin, self.xmin + self.width, self.ymin + self.height, self.class_label)
	
def parseBoxesToList(model_result):
    boxes = model_result[0].boxes
    parse = list()
    for i in range(len(boxes)):
        xy = boxes[i].xyxy[0].tolist()
        parse.append({'x': xy[0], 'y': xy[1], 'w': xy[2], 'h': xy[3], 'confidence': float(boxes.conf[i]), 'class': int(boxes.cls[i])})
    return parse
    
    
boxx = parseBoxesToList(model_result)
def toBBList(boxx):
    return [BoundBox(i) for i in boxx]


[print(i) for i in toBBList(boxx)]
print()




import cv2
import time

# Access the camera
cap = cv2.VideoCapture(0)

# Initialize variables for calculating FPS
fps_start_time = time.time()
fps_frames = 0

while True:
    # Get each frame as an image
    ret, frame = cap.read()
    
    # Calculate FPS
    fps_frames += 1
    fps = 0
    if time.time() - fps_start_time >= 0:
        fps = fps_frames / (time.time() - fps_start_time)
        fps_start_time = time.time()
        fps_frames = 0

    # Overlay FPS on the image
    cv2.putText(frame, f'FPS: {int(fps)}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    result = toBBList((modelresult := parseBoxesToList(model(frame, verbose=False))))
    # print(modelresult)
    for box in result:
        # if box.get_label() is None:
        #     continue
        if box.get_confidence() < 0.5:
            continue
        
        xmin, ymin, xmax, ymax = (w := [int(_) for _ in box.get_coordinates()])
        cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (255, 0, 0), 2)
        cv2.putText(frame, str(box.get_label()), ((xmin + xmax) // 2, (ymin + ymax) // 2), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 2)
        cv2.putText(frame, str(box.get_confidence()), (xmin + 50, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    # Show the image
    cv2.imshow('frame', frame)
    
    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()


