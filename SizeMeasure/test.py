import cv2 
import numpy as np 
from helper import helper

class tracker():
    def __init__(self, range, num):
        self.range = range 
        self.num = num
        self.track()
    def nothing(self, x):
        pass 
    
    def track(self): 
        for i in range(self.num): 
            cv2.createTrackbar(str(i), 'img', self.range[i][0], self.range[i][1], 
            self.nothing)
        
    def trackPos(self):
        val = np.zeros(self.num)
        for i in range(self.num):
            val[i]= cv2.getTrackbarPos(str(i), 'img')
        return val

img = cv2.imread('C:\\ComputerVision\\OpenCV\\Basics\\SizeMeasure\\Pills.jpg')
cv2.namedWindow("img")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
tracker = tracker(((1,255),(0,255)), 2)
while True: 
    val = np.array(tracker.trackPos(), dtype=np.int32)
    print(val)
    img = cv2.GaussianBlur(img, (val[0], val[0]), val[1])
    cv2.imshow('img', img)
    k = cv2.waitKey(0)
    if k == ord('q'):
        cv2.destroyAllWindows()
        break 

