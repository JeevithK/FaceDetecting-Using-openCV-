import cv2
trained = cv2.CascadeClassifier('haarcascade')
img=cv2.imread('rdj2.jpg')
grayscaleimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face_coordinates=trained.detectMultiScale(grayscaleimg)
print(face_coordinates)


cv2.imshow("this is jeevith",grayscaleimg)
cv2.waitKey()
print("code completed")
#convert into the grayscale

 
 
