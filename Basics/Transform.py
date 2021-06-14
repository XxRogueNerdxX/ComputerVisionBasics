import numpy as np 
import cv2 as cv 

'''
img = cv.imread('smarties.png', 0)

_, mask = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)

kernal = np.ones((2,2), dtype= np.uint8)

dilate = cv.dilate(mask, kernal, iterations= 2)
erode = cv.erode(mask, kernal, iterations=2)
morph = cv.morphologyEx(mask, cv.MORPH_GRADIENT, kernal)
cv.imshow('img', img)
cv.imshow('mask', mask)
cv.imshow('dilate', dilate)
cv.imshow('erode', erode)
cv.imshow('morph', morph)
cv.waitKey(0)
cv.destroyAllWindows()
'''

def findall_transform(img, kernal, iterations = None, mask = False, threshold = 127):
    kernel = np.ones(kernal, np.uint8)
    if mask: 
        _, mask = cv.threshold(img, threshold, 255, cv.THRESH_BINARY_INV )

    else : 
        mask = img

    dilate = cv.dilate(mask, kernel, iterations= 2)
    erode = cv.erode(mask, kernel, iterations=2)
    morph = cv.morphologyEx(mask, cv.MORPH_GRADIENT, kernel)
    opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
    closing = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)
    top_hat = cv.morphologyEx(mask, cv.MORPH_TOPHAT, kernel)
    black_hat = cv.morphologyEx(mask, cv.MORPH_BLACKHAT, kernel)

    cv.imshow('image', img)
    cv.imshow('dilate', dilate)
    cv.imshow('erode', erode)
    cv.imshow('morph', morph)
    cv.imshow('opening', opening) 
    cv.imshow('closing', closing)
    cv.imshow('top_hat', top_hat)
    cv.imshow('black_hat', black_hat)

    cv.waitKey(0)
    cv.destroyAllWindows()

img = cv.imread('lena.jpg', 0)
findall_transform(img,[4,4])
    
    
