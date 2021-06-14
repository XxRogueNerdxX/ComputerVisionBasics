from scipy.spatial import distance as dist 
from imutils import perspective
from imutils import contours 
import numpy as np 
import imutils
import cv2 

def midpoint(pA, pB):
    return ((pA[0] + pB[0]) * 0.5, (pA[1] + pB[1])* 0.5)

path  = 'C:\\ComputerVision\\OpenCV\\Basics\\SizeMeasure\\Pills.jpg'
image = cv2.imread(path)
orgi = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (3,3),0)
gray = cv2.Canny(gray, 100, 200) #50, 100

cnts, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = sorted(cnts, key =  cv2.contourArea, reverse=True)
pixel = None 
for c in cnts: 
    if cv2.contourArea(c) < 50: 
        continue
    box = cv2.minAreaRect(c)
    box = cv2.boxPoints(box)
    box = np.array(box, "int")
    cv2.drawContours(orgi, [box.astype("int")], -1, (0,255,0),2)

    for (x,y) in box:
        cv2.circle(orgi, (int(x), int(y)), 5, (0,0,255), -1)

    (tl, tr, br, bl) = box
    (tltrx, tltry) = midpoint(tl, tr)
    (blbrx, blbry) = midpoint(bl, br)

    (tlblx, tltbly) = midpoint(tl,bl)
    (trbrx, trbry) = midpoint(tr, br)

    cv2.circle(orgi, (int(tltrx), int(tltry)), 5, (255, 0,0), -1)
    cv2.circle(orgi, (int(blbrx), int(blbry)), 5, (255, 0,0), -1)
    cv2.circle(orgi, (int(tlblx), int(tltbly)), 5, (255, 0, 0), -1)
    cv2.circle(orgi, (int(trbrx), int(trbry)), 5, (255,0,0), -1)

    cv2.line(orgi, (int(tltrx), int(tltry)), (int(blbrx), int(blbry)), (0,255,0), 3)
    cv2.line(orgi, (int(tlblx), int(tltbly)), (int(trbrx), int(trbry)), (0, 255, 0), 3)

    dA = dist.euclidean((tltrx,tltry), (blbrx , blbry))
    dB = dist.euclidean((tlblx , tltbly) ,(trbrx , trbry))

    if pixel is None: 
        pixel = dB / 0.955
    dimA = dA/ pixel
    dimB = dB/ pixel 

    cv2.putText(orgi, "{:.1f}in".format(dimA),
		(int(tltrx - 15), int(tltry - 10)), cv2.FONT_HERSHEY_SIMPLEX,
		0.65, (255, 255, 255), 2)
    cv2.putText(orgi, "{:.1f}in".format(dimB),
		(int(trbrx + 10), int(trbry)), cv2.FONT_HERSHEY_SIMPLEX,
		0.65, (255, 255, 255), 2)


cv2.imshow("img", orgi)
cv2.waitKey(0)