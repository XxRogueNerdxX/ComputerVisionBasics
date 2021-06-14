import cv2 
import numpy as np 


#removing and merging images 
'''
img =  cv2.imread(r'C:\\ComputerVision\\OpenCV\\Basics\\lena.jpg')
print(img.size)
print(img.shape)
print(img.dtype)

b,g,r = cv2.split(img)
cv2.imshow('ig', img)
r = cv2.merge((r,r,r))
cv2.imshow('image', r )
cv2.imshow('imag', b )
cv2.imshow('ma', g )
cv2.waitKey()
cv2.destroyAllWindows()

'''
#adding images and watermark 
'''
img = cv2.imread('messi5.jpg')
img_2 = cv2.imread('opencv-logo.png')


img = cv2.resize(img, (512,512))
img_2 = cv2.resize(img_2, (512, 512))


dest = cv2.addWeighted(img, .9, img_2, .5, 10)
cv2.imshow('image', dest)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''


#Track Bar
'''

def nothing(x):
    print(x)
img = np.zeros((300, 512, 3), np.uint8)

cv2.namedWindow('image')

cv2.createTrackbar('B', 'image', 0,  255, nothing)
cv2.createTrackbar('G', 'image', 0,  255, nothing)
cv2.createTrackbar('R', 'image', 0,  255, nothing)
cv2.createTrackbar('switch','image', 0,1, nothing)

while(True):
    cv2.imshow('image', img)
    b = cv2.getTrackbarPos('B', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    r = cv2.getTrackbarPos('R', 'image')
    switch = cv2.getTrackbarPos('switch', 'image')     
    k = cv2.waitKey(1)
    if  k == ord('q'):
        cv2.destroyAllWindows()
        break
    if switch == 0:
        img[:] = 0
    else : 
        img[:] = [b,g,r] 
'''

