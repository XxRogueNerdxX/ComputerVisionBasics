import cv2
import numpy as np 

def transform(img, points):
    rect = np.zeros((4,2), np.float32)
    s = points.sum(axis=1)
    rect[0] = points[np.argmin(s)]
    rect[2] = points[np.argmax(s)]

    diff = np.diff(points, axis = 1)
    rect[1] = points[np.argmin(diff)]
    rect[3] = points[np.argmax(diff)]

    (tl, tr, br, bl) = rect
    widthA = np.linalg.norm(tl - tr)
    widthB = np.linalg.norm(bl - br)

    heightA = np.linalg.norm(tl - bl)
    heightB = np.linalg.norm(tr - br)

    width = max(int(widthA), int(widthB))
    height = max(int(heightA), int(heightB))

    dist = np.array([
        [0,0],
        [width -1, 0], 
        [width - 1, height -1],
        [0, height -1]
    ], "float32")

    M = cv2.getPerspectiveTransform(rect, dist)
    wrapped = cv2.warpPerspective(img, M, (width, height))
    return wrapped




