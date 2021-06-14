import numpy as np 
import cv2 as cv 



def Smooth(img, kernal):
    kernel = np.ones(kernal, np.float32) / 25
    filter = cv.filter2D(img, -1, kernel) #2D convolutions 
    blur = cv.blur(img, (5,5)) #similar to filter2d
    gblur = cv.GaussianBlur(img, (5,5), 0) #Gives more importace to the center and reduces as we move 
    median = cv.medianBlur(img, 5) #good to reduce salt and peper grains 
    biletarlfilter = cv.bilateralFilter(img, 9, 75, 75) #blurs but preserves the images 


    cv.imshow('filter2D', filter)
    cv.imshow('blur', blur)
    cv.imshow('gblur', gblur)
    cv.imshow('median', median) 
    cv.imshow('bilateral', biletarlfilter)
    cv.waitKey(1)

    cv.destroyAllWindows()

img = cv.imread('lena.jpg')
Smooth(img, (5,5))