import cv2 as cv
import numpy as np

cap = cv.VideoCapture('C:\\ComputerVision\\OpenCV\\Basics\\vtest.avi')

ret, frame1 = cap.read()
_ , frame2 = cap.read()

while cap.isOpened() : 
    diff = cv.absdiff(frame1, frame2)
    gray = cv.cvtColor(diff, cv.COLOR_RGB2GRAY)
    blur = cv.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv.threshold(blur, 20, 255, cv.THRESH_BINARY)
    dilated = cv.dilate(thresh,None, iterations=3)
    #dilated = cv.erode(thresh,None, iterations=3)
    contours, _ = cv.findContours(dilated, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # cv.imshow("normal", diff)
    # cv.imshow("blur", blur)
    # cv.imshow("thresh", thresh)
    # cv.imshow("dilated",dilated)
    # cv.imshow("erode",erode)
    for contour in contours :
        (x, y, w, h) = cv.boundingRect(contour)

        if cv.contourArea(contour) < 900: 
            continue 
        cv.rectangle(frame1, (x,y), (x+w, y+h), (0,255,0), 2)
        cv.imshow("feed", frame1)

    frame2 = frame1
    _, frame1 = cap.read() 

        
    if cv.waitKey(1) == ord('q') :
        break 
cap.release()
cv.destroyAllWindows()