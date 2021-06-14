
import cv2
import numpy as np 
import imutils
import os 

tracker = cv2.TrackerCSRT_create() 
# KCF: Fast and accurate
# CSRT: More accurate than KCF but slower
# MOSSE: Extremely fast but not as accurate as either KCF or CSRT

cap = cv2.VideoCapture(1)
intBB = None
while(True):
    ret, frame = cap.read()
    frame = imutils.resize(frame, width=500)
    (H, W) = frame.shape[:2]

    

    if intBB is not None:
        (sucess, box)  = tracker.update(frame)
        if sucess : 
            (x, y, w, h) = [int(v) for v in box] 
            cv2.rectangle(frame, (x,y), (w + x, h + y), (0, 255, 0), 2)

    cv2.imshow("feed", frame)
    key = cv2.waitKey(1) 
    if key == ord("s"): 
        intBB = cv2.selectROI("feed", frame, fromCenter=False, showCrosshair= True) 
        tracker.init(frame, intBB)
    
    elif key == ord("q"):
        cap.release()

    
cv2.destroyAllWindows()

