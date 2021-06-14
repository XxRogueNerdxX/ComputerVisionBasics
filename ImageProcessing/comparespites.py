from scipy.spatial import distance as dist 
import cv2 
import pickle
import imutils
import numpy as np 
from pokimon import zern

class search():
    def __init__(self, index): 
        self.index = index
    
    def search(self, queryfeatures):
        results = {}
        for (k, features) in self.index.items(): 
            d = dist.euclidean(queryfeatures, features)
            results[k] = d 
        
        results = sorted([(v,k) for (v,k) in results.items()])
        return results 

zern_sprites = 'C:\\ComputerVision\\OpenCV\\Basics\\ImageProcessing\\zern_spites\\lol.txt'
img = cv2.imread('C:\\ComputerVision\\OpenCV\\Basics\\ImageProcessing\\cropperImg.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = imutils.resize(img, width=64)
index = open(zern_sprites, "rb").read()
index = pickle.loads(index)
thresh = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
	cv2.THRESH_BINARY_INV, 15, 5)

# kernel = np.ones((3,3), np.uint8)
# lap = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
# _, lap = cv2.threshold(lap, 20, 255, cv2.THRESH_BINARY)
cv2.imshow("img1", thresh)

outline = np.zeros(img.shape, dtype = "uint8")
cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[0]
cv2.drawContours(outline, [cnts], -1, 255, -1)

desc = zern(21)
query = desc.describe(outline)
searcher = search(index)
results = searcher.search(query)
print(results[0][0])
# print "That pokemon is: %s" % results[0][1].upper()
cv2.imshow("img", outline)
cv2.waitKey(0)
