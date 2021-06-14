import cv2 
import numpy as np

image = cv2.imread(r'C:\\ComputerVision\\OpenCV\\Basics\\lena.jpg')
lap = cv2.Laplacian(image, cv2.CV_64F)
lap =   np.absolute(lap)
cv2.imshow("img", lap)
cv2.waitKey(0)
cv2.destroyAllWindows()