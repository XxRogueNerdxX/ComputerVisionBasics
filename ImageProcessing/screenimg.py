from os import read
import cv2 
import numpy as np 
import imutils
import matplotlib.pyplot as plt 
from skimage import exposure

img = cv2.imread('C:\\ComputerVision\\OpenCV\\Basics\\ImageProcessing\\gameboy-query.jpg')
cv2.imshow("img", img)
#cv2.waitKey(0)

org = img.copy()
ratio = img.shape[0]/300.0

img = imutils.resize(img, height=300)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.bilateralFilter(img, 9, 17,17)
img = cv2.Canny(img, 30,200)
cntr = cv2.findContours(img.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cntr = imutils.grab_contours(cntr)
cntr = sorted(cntr, key=cv2.contourArea,reverse=True)[:10]
screenCnt = None 
for c in cntr:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.015*peri, True)
    if len(approx) == 4:
        screenCnt = approx
        break 

pts = screenCnt.reshape(4,2)
rect = np.zeros((4,2), dtype= "float32")

s = pts.sum(axis = 1)
rect[0] = pts[np.argmin(s)]
rect[2] = pts[np.argmax(s)]

d = np.diff(pts, axis = 1)
rect[1] = pts[np.argmin(d)]
rect[3] = pts[np.argmax(d)]

rect *= ratio

(tl, tr, bl, br) = rect 
widthA = np.sqrt((br[0] - bl[0]) ** 2 + (br[1] - bl[1]) ** 2)
widthB = np.sqrt((tr[0] - tl[0]) ** 2 + (tr[1] - tl[1]) ** 2)

heightA = np.sqrt((br[0] - tr[0]) ** 2 + (br[1] - tr[1]) ** 2)
heightB = np.sqrt((bl[0] - tl[0]) ** 2 + (bl[1] - tl[1]) ** 2)

maxWidth = max(int(widthA), int(widthB))
maxHeight = max(int(heightA), int(heightB))

dst = np.array([

    [0,0], 
    [maxWidth -1, 0], 
    [maxWidth -1, maxHeight -1], 

    [0, maxHeight -1]
], dtype = "float32")
M = cv2.getPerspectiveTransform(rect, dst)
wrap = cv2.warpPerspective(org, M, (maxWidth, maxHeight))

wrap = cv2.cvtColor(wrap, cv2.COLOR_BGR2GRAY)
wrap = exposure.rescale_intensity(wrap, out_range=(0,255))

(h, w) = wrap.shape[:2]
(dx, dy) = (int(w * 0.4) , int(h * 0.45))
crop = wrap[10:dy, w - dx:w]
#cv2.imwrite("cropperImg.png", crop)
cv2.imshow("img1",  imutils.resize(crop, height = 300))

cv2.waitKey(0)


