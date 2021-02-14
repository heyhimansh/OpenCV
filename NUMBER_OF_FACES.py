##face detection
##face detection
##face detection
##face detection

import cv2 as cv
import numpy as np
img= cv.imread('photos/N3.jpg')
cv.imshow(' developing image ',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)
haar_cascade = cv.CascadeClassifier('haarcascades.xml')
face_rect= haar_cascade.detectMultiScale(gray,scaleFactor = 1.1 ,minNeighbors=2,minSize=(30, 30))
print('NUMBER OF FACES FOUND = ' ,len(face_rect))

for (x,y,w,h) in face_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,0,255),thickness = 2)

for (x,y,w,h) in face_rect:
    cv.rectangle(gray,(x,y),(x+w,y+h),(0,0,255),thickness = 2)
        
cv.imshow('detected faces gray',gray)    
cv.imshow('detected faces',img)