import cv2 as cv
import numpy as np 

def image_stats(image):
	# compute the mean and standard deviation of each channel
	(l, a, b) = cv.split(image)
	(lMean, lStd) = (l.mean(), l.std())
	(aMean, aStd) = (a.mean(), a.std())
	(bMean, bStd) = (b.mean(), b.std())
	# return the color statistics
	return (lMean, lStd, aMean, aStd, bMean, bStd)

source = cv.imread('C:\\ComputerVision\\OpenCV\\Basics\\ocean_day.jpg')
target = cv.imread('C:\\ComputerVision\OpenCV\\Basics\\ocean_sunset.jpg')

source = cv.cvtColor(source, cv.COLOR_BGR2LAB)
target = cv.cvtColor(target, cv.COLOR_BGR2LAB)

(lMeanSrc, lStdSrc, aMeanSrc, aStdSrc, bMeanSrc, bStdSrc) = image_stats(source)
(lMeanTar, lStdTar, aMeanTar, aStdTar, bMeanTar, bStdTar) = image_stats(target)

(l, a, b) = cv.split(target)
l = np.subtract(l, lMeanTar)
a = np.subtract(a, aMeanTar)
b = np.subtract(b, bMeanTar)

l = (lStdTar / lStdSrc) * l
a = (aStdTar / aStdSrc) * a
b = (bStdTar / bStdSrc) * b

l += lMeanSrc
a += aMeanSrc
b += bMeanSrc

l = np.clip(l, 0, 255)
a = np.clip(a, 0, 255)
b = np.clip(b, 0, 255)

transfer = cv.merge([l, a, b])
transfer = cv.cvtColor(transfer.astype("uint8"), cv.COLOR_LAB2BGR)
cv.imshow("img", transfer)
cv.waitKey(0)
cv.destroyAllWindows()

# source_mean, source_std = cv.meanStdDev(source)
# target_mean, target_std = cv.meanStdDev(target)



print('lol')