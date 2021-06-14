from sklearn.base import BaseEstimator
from sklearn.cluster import KMeans
import cv2 
import numpy as np 
import matplotlib.pyplot as plt 

def histogram(clt):
    lables = np.arange(0, len(np.unique(clt.labels_))+1)
    hist, _ = np.histogram(clt.labels_, lables)
    hist = np.divide(hist, sum(hist))
    return hist 

def plotter(hist, centers):
    bar = np.zeros((50,300,3), dtype = np.uint8)
    startX = 0 
    for (percentage ,color) in zip(hist, centers):
        endX = startX + (percentage * 300)
        cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),
        color.astpye("uint8").tolist(), -1)

    plt.figure()
    plt.axis("off")
    plt.imshow(bar)
    plt.show()

img = cv2.imread('C:\\ComputerVision\\OpenCV\\Basics\\ImageProcessing\\jp.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = img.reshape(img.shape[0] * img.shape[1], 3)
clusters = 3
clt = KMeans(clusters)
clt.fit(img)
hist = histogram(clt)
plotter(hist, clt.cluster_centers_)
