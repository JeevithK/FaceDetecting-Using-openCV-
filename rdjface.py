import cv2

from random import randrange

trained = cv2.CascadeClassifier('haarcascade.xml')

#print("whats up")

#img=cv2.imread('boys.jpg')

webcam = cv2.VideoCapture(0)

while True:
    successful_frame_read, frame=webcam.read()
    grayscaleimg=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    facecord=trained.detectMultiScale(grayscaleimg)
    for (x,y,w,h) in facecord:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.imshow('this is jeevith',frame)
        key=cv2.waitKey(1)
        if key==81 or key==113:
            break
webcam.release()

print("code completed")

 
#[[ 81  62 133 133]
 #[104 162  96  96]]

