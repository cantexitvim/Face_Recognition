import cv2
import os

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

font=cv2.FONT_HERSHEY_COMPLEX

names=['Mansi']

cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while True:
    _,img=cap.read()

    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces=face_cascade.detectMultiScale(gray,1.1,4)

    for (x, y, w, h), name in zip(faces, names):
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(img, name, (x, y-10), font, 0.9, (255, 255, 255), 2)

    cv2.imshow('img',img)
    
    k=cv2.waitKey(30)&0xff
    if k==27:
        break

cap.release()
cv2.destroyAllWindows()
