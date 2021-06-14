from typing import OrderedDict
import numpy as np 
import cv2 as  cv 

def nothing(x):
    pass
img = cv.imread('messi5.jpg')
cv.namedWindow('img')
cv.createTrackbar('r', 'img', 0, 255, nothing)
cv.createTrackbar('g', 'img', 0, 255, nothing)
cv.createTrackbar('b', 'img', 0, 255, nothing)

while(True):
    r = cv.getTrackbarPos('r', 'img')
    g = cv.getTrackbarPos('g', 'img')
    b = cv.getTrackbarPos('b', 'img')
    
    img[:,:,2] = r
  
    #img[:,:,0] = b
    cv.imshow('mg', img)
    k = cv.waitKey(1)
    if k == ord('q'):
        break 

cv.destroyAllWindows()