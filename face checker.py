import cv2
import numpy as np
model = cv2.face.LBPHFaceRecognizer_create()
model = cv2.face.EigenFaceRecognizer_create()
model = cv2.face.FisherFaceRecognizer_create()

def detect_face(img_path):
    img = cv2.imread(img_path)
    detected_faces = faceCascade.detectMultiScale(img, 1.3, 5)
    x,y,w,h = detected_faces[0]
    img = img[y:y+h, x:x+w]
    img = cv2.resize(img, (224,224))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img
face_db = [
    "deepface/tests/dataset/img1.jpg",
    "deepface/tests/dataset/img3.jpg",
    "deepface/tests/dataset/img8.jpg",
    "deepface/tests/dataset/img13.jpg",
    "deepface/tests/dataset/img30.jpg",
    "deepface/tests/dataset/img44.jpg"
    ]
faces = []
for img_path in face_db:
    print(img_path)
    img = detect_face(img_path)
    faces.append(img)
ids = np.array([i for i in range(0,len(faces))])

