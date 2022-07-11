import cv2
import numpy 

img = cv2.imread('img1.jpg')

img = cv2.GaussianBlur(img, (3, 3), 0)


img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.Canny(img, 30, 30)

carnell = numpy.ones((5, 5), numpy.uint8)

img = cv2.dilate(img, carnell, iterations=1)

cv2.imshow('Pictures One', img)

cv2.waitKey(0)
	
	
