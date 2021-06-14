import mahotas
import os
import cv2
from imutils.paths import list_images
import imutils
import pickle
import numpy as np 


sprites = 'C:\\Users\\Rakesh\\Downloads\\generation-1.tar\\pokemon\\main-sprites\\red-blue\\gray'	
final_loc = 'C:\\ComputerVision\\OpenCV\\Basics\\ImageProcessing\\zern_spites\\lol.txt'
image_types = (".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff")
index  = {}
class zern():
	def __init__(self, radius):
		self.radius = radius
	
	def describe(self, cnt):
		return  mahotas.features.zernike_moments(cnt, self.radius)

des = zern(21)	
for root, dir, files in os.walk(sprites):

	for file in files:
		if file[file.find('.'):].endswith(image_types):
			path = os.path.join(root, file)
			pokemon = file[:file.find(".")]
			img  = cv2.imread(path)
			img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
			img = cv2.copyMakeBorder(img, 15, 15, 15, 15,
			cv2.BORDER_CONSTANT, value = 255)
			thresh = cv2.bitwise_not(img)
			thresh[thresh > 0] = 255
			outline = np.zeros(img.shape, dtype = "uint8")
			cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
				cv2.CHAIN_APPROX_SIMPLE)
			cnts = imutils.grab_contours(cnts)
			#cnts2 = sorted(cnts, key = cv2.contourArea, reverse = True)[0]
			cv2.drawContours(outline, cnts, -1, 255, -1)
			moments = des.describe(outline)
			index[pokemon] = moments

		else :
			continue
	f = open(final_loc, "wb")
	f.write(pickle.dumps(index))
	f.close()
			
