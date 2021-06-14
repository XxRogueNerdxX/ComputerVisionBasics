import cv2 
import cv2 
from skimage.exposure import is_low_contrast

img = cv2.imread()
img  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
threshold = 10 #change this

if is_low_contrast(img, threshold):
    print("low contrast")
else : 
    print("meh ur good")