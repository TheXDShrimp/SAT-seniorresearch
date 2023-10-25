import cv2

# Get the video capture object
cap = cv2.VideoCapture(0)

# Check if the camera is opened
if not cap.isOpened():
  print("Error opening the camera")
  exit(1)

# Capture the frame
ret, frame = cap.read()

print(ret)
# Display the frame
cv2.imshow("Frame", frame)
print(frame)

# Wait for a key press
cv2.waitKey(0)

# Release the capture object
cap.release()

# Close all windows
cv2.destroyAllWindows()
