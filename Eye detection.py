import numpy as np
import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

while True:
    ret, frame = cap.read(0)
    cv2.cvtColor
    
    cv2.imshow('frame', frame)
    if cv2.waitkey(1) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()

opencv-contrib-python
