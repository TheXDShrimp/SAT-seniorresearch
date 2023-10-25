import torch
import numpy as np
import pandas as pd

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# predict on cars.jpg and display it

results = model("cars.jpg", save=True)
print(results.pandas())

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