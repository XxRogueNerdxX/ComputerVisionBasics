from imutils.convenience import skeletonize
from centroid_Tracker import CentroidTracker
import cv2 
import imutils
import dlib
import numpy as np  


class TrackableObject:
	def __init__(self, objectID, centroid):
		# store the object ID, then initialize a list of centroids
		# using the current centroid
		self.objectID = objectID
		self.centroids = [centroid]
		# initialize a boolean used to indicate if the object has
		# already been counted or not
		self.counted = False


model = "C:\\ComputerVision\\OpenCV\\Basics\\Classification_Easy_DNN\\MobileNetSSD_deploy.caffemodel"
prototxt = 'C:\ComputerVision\OpenCV\Basics\\bvlc_googlenet.prototxt'

net = cv2.dnn.readNetFromCaffe(prototxt, model)
cap = cv2.VideoCapture('C:\\ComputerVision\\OpenCV\\Basics\\Classification_Easy_DNN\\example01.mp4')
ct = CentroidTracker()

CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
	"bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
	"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
	"sofa", "train", "tvmonitor"]
trackableObjects = {}
min_confidence = 0.2 
skip_frames = 30
total_frames = 0
w = None
h = None
while True: 
    ret, frame = cap.read()
    status = "Waiting"
    frame = imutils.resize(frame, width=500)
    rgb_frame = cv2.cvtColor(cv2.COLOR_BGR2RGB)
    if w == None: 
        (h,w) = cv2.shape[:2]
    
    rects = []

    if total_frames % skip_frames:
        status = "Detecting"
        trackers = []
        blob = cv2.dnn.blobFromImage(frame, 0.007843, (w,h), 127.5)
        net.setInput(blob)
        detections = net.forward()
        for i in np.array(detections.shape[2]):
            
            confidence = detections[0,0,i,2]
            if confidence > min_confidence:
                index = int(detections[0,0,i,1])
                if CLASSES[index] != 'person':
                    continue
                else :
                    box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                    (startX, startY, endX, endY) = box.astype("int")
                    tracker = dlib.correlation_tracker()

                    rect = dlib.rectangle(startX, startY, endX, endY)
                    tracker.start_track(rgb_frame, rect)
                    trackers.append(tracker)
            
    else : 
       for tracker in trackers :
            status = "Tracking"
            tracker.update(rgb_frame)
            pos = tracker.get_position()

            startX = int(pos.left())
            startY = int(pos.top())
            endX = int(pos.right())
            endY = int(pos.bottom())

            rects.append((startX, startY, endX, endY))
            cv2.line(frame, (0, h // 2), (w, h // 2), (0, 255, 255), 2)
            objects = ct.update(rects)
            for(objectID, centroid) in objects.items():
                to = trackableObjects.get(objectID, None)
                if to is None:
			        to = TrackableObject(objectID, centroid)
                    
                



                    

