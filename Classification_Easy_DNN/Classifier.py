import numpy as np
import cv2 
import os
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--prototext", default='C:\\ComputerVision\\OpenCV\\Basics\\Classification_Easy_DNN\\bvlc_googlenet.prototxt')
ap.add_argument("-m", "--model", default='C:\\ComputerVision\\OpenCV\\Basics\\Classification_Easy_DNN\\bvlc_googlenet.caffemodel')
args = vars(ap.parse_args())
img = cv2.imread("C:\\ComputerVision\\OpenCV\\Basics\\Classification_Easy_DNN\\dog.jpg")
rows = open("synset_words.txt")
rows = rows.read()
rows = rows.strip()
rows = rows.split("\n")
classes = [r[r.find(" ") + 1:].split(",")[0] for r in rows]
blog = cv2.dnn.blobFromImage(img, 1, (244,244), (104, 117, 123))
net = cv2.dnn.readNetFromCaffe(args["prototext"], args["model"])
net.setInput(blog)
preds = net.forward()
classes=  np.array(classes)
idxs = np.argsort(preds[0])[::-1][:5]
print(classes[idxs])