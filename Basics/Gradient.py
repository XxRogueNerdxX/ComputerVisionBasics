import numpy as np 
import cv2 as cv 

def Gradient(img):
    img = cv.Canny(img, 100, 200)
    cv.imshow('img', img)
    cv.waitKey(0)
    cv.destroyAllWindows()

def Pyramind(img):
    layer = img
    for i in range(6):
        layer = cv.pyrDown(layer)
        cv.imshow(str(i), layer) 
    cv.waitKey(0)
    cv.destroyAllWindows()


def lap_pyramind(img):
    layer = img 
    gp = []
    for i in range(6):
        gp.append(layer)
        layer = cv.pyrDown(layer)

    for i in range(5,0,-1):
        ext = cv.pyrUp(gp[i])
        lap = cv.subtract(gp[i - 1] , ext)
        cv.imshow(str(i), lap)

    cv.waitKey(0)
    cv.destroyAllWindows()  
    

img = cv.imread('lena.jpg')
lap_pyramind(img)   