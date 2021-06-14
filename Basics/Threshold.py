import cv2 as cv 
import numpy as np 

# #ADAPTIVE THRESHOLD
# img = cv.imread('lena.jpg',0)
# th1 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 21, 10)
# th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 9, 4)
# cv.imshow('th1', th1)
# cv.imshow('th2', th2)
# cv.imshow('img', img)

# cv.waitKey(0)
# cv.destroyAllWindows()

#SIMPLE THRESHOLD 

img = cv.imread('C:\\ComputerVision\\OpenCV\\Basics\\gradient.png', 0)
_, th1 = cv.threshold(img, 50, 255, cv.THRESH_BINARY) #when pixel value goes over 50(given) it would put white or black
_, th2 = cv.threshold(img, 50, 255, cv.THRESH_BINARY_INV)
_, th3 = cv.threshold(img, 50, 255, cv.THRESH_TRUNC) #after the point thresold the color is kept common 
_, th4 = cv.threshold(img, 50, 255, cv.THRESH_TOZERO) 
 
cv.imshow('th1', th1)
cv.imshow('th2', th2)
cv.imshow('th3', th3)
cv.imshow('th4', th4)
cv.imshow('img', img)

cv.waitKey(0)
cv.destroyAllWindows()