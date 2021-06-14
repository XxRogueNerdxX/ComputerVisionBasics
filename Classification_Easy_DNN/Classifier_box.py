import cv2 
import numpy as np 

model = "C:\\ComputerVision\\OpenCV\\Basics\\Classification_Easy_DNN\\MobileNetSSD_deploy.caffemodel"
prototxt = 'C:\ComputerVision\OpenCV\Basics\\bvlc_googlenet.prototxt'
img = cv2.imread('C:\\ComputerVision\\OpenCV\\Basics\\Classification_Easy_DNN\\example_01.jpg')
def_confidence = 0.2

CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
	"bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
	"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
	"sofa", "train", "tvmonitor"]
COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))
(h, w) = img.shape[:2]
net = cv2.dnn.readNetFromCaffe(prototxt, model)
blob = cv2.dnn.blobFromImage(cv2.resize(img, (300, 300)), 0.007843, (300, 300), 127.5)
net.setInput(blob)
detections = net.forward()
for i in np.arange(0, detections.shape[2]):
    confidence = detections[0, 0, i, 1]
    if confidence > def_confidence:
        index = int(detections[0,0,i,1])
        box = (detections[0, 0, i, 3:7]) * np.array([w, h, w, h])
        (startX, startY, endX, endY) = box.astype("int")
        label = (CLASSES[index], confidence * 100)

        print(label)
        cv2.rectangle(img, (startX, startY), (endX, endY),
            COLORS[index], 2)
        y = startY - 15 if startY - 15 > 15 else startY + 15
        cv2.putText(img, str(label), (startX, y),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[index], 2)

# show the output image

cv2.imshow("Output", img)
cv2.waitKey(0)