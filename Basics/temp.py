
import numpy as np 
import cv2 as cv 

cap = cv.VideoCapture(1)
img =  cv.imread('forest.jpg')
while(True):
    _, frame = cap.read()
    cv.imshow('frame', frame)
    img = cv.resize(img, (512, 512))
    gre_frame = cv.resize(frame, (512, 512))
    gre_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    gre_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    _, th1 = cv.threshold(gre_frame, 120, 255, cv.THRESH_BINARY_INV)
    _, th2 = cv.threshold(gre_frame, 120, 255, cv.THRESH_BINARY)
    cv.imshow('mask', th1)
    fin = cv.bitwise_and(frame, frame, mask = th1)
    bgm = np.zeros((fin.shape),np.uint8)
    bgm[:]  = (0,255, 0)
    bgm = cv.resize(bgm , (512,512))
    th2 = cv.resize(th2, (512, 512)) 


    bgm = cv.bitwise_and(img, img ,mask = th2)
    cv.imshow('mask2', bgm)
    fin = cv.resize(fin, (512, 512))
    fin = cv.add(fin, bgm)
    cv.imshow('final', fin)

    key = cv.waitKey(1)
    if key == ord('q'):
        break
cap.release()
cv.destroyAllWindows()

    