# Run pip install opencv-python
# Run pip install dlib

import cv2
import dlib

# Get camera
cap = cv2.VideoCapture(0)

detector = dlib.get_frontal_face_detector()

# Run this code until esc key is pressed
while True:
    _, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    for face in faces:
        x, y = face.left(), face.top()
        x1, y1 = face.right(), face.bottom()
        cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)

    cv2.inshow("Frame", frame)

    key = cv2.waitkey(1)
    if key==27:
        break

cap.realease()
cap.destroyAllWindows()