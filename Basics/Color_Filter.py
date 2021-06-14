import cv2
import numpy as np 



def nothing(x):
    pass
#img = cv2.imread('smarties.png')
cap = cv2.VideoCapture(0)

cv2.namedWindow('Color_Filter')
cv2.createTrackbar('Hue_l','Color_Filter', 0,255,nothing)
cv2.createTrackbar('Sat_l','Color_Filter', 0,255,nothing)
cv2.createTrackbar('Bri_l','Color_Filter', 0,255,nothing)

cv2.createTrackbar('Hue_h','Color_Filter', 255,255,nothing)
cv2.createTrackbar('Sat_h','Color_Filter', 255,255,nothing)
cv2.createTrackbar('Bri_h','Color_Filter', 255,255,nothing)

while(True):
    _, img  = cap.read()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    l_h = cv2.getTrackbarPos('Hue_l', 'Color_Filter')
    l_s = cv2.getTrackbarPos('Sat_l', 'Color_Filter')
    l_br = cv2.getTrackbarPos('Bri_l', 'Color_Filter')

    h_h = cv2.getTrackbarPos('Hue_h', 'Color_Filter')
    h_s = cv2.getTrackbarPos('Sat_h', 'Color_Filter')
    h_br = cv2.getTrackbarPos('Bri_h', 'Color_Filter')

    l_b = np.array([l_h, l_s, l_br])
    h_b = np.array([h_h, h_s, h_br])

    mask = cv2.inRange(hsv, l_b, h_b)

    res = cv2.bitwise_and(img, img, mask = mask)

    cv2.imshow('img', res)
    cv2.imshow('imge', mask)
    cv2.imshow('im', img)

    k = cv2.waitKey(1)
    if k == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break