from os import scandir
import cv2
import numpy as np 
from skimage.filters import threshold_local
from Perspective import transform

img = cv2.imread('C:\\ComputerVision\\OpenCV\Basics\\doc_scanner\\receipt-scanned.jpg')
org = img.copy()
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(img, (3,3), 0)
img = cv2.Canny(img, 120,250)
cntr = cv2.findContours(img.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cntr = cntr[0]
sort = sorted(cntr, key = cv2.contourArea, reverse= True)[:5]
screen = None 
for c in sort:
    #img = cv2.drawContours(org, [c], -1, (0,255,0), 3)
    M = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.004* M, True)
    if len(approx) == 4:
        screen = approx
        break

wrapped  = transform(org, np.array(screen).reshape(4,2))
wrapped = cv2.cvtColor(wrapped, cv2.COLOR_BGR2GRAY)
T = threshold_local(wrapped, 11, 'gaussian', 10)
wrapped = (wrapped > T).astype("uint8") * 255
cv2.imshow("img", wrapped)
cv2.waitKey(0)



