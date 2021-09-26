import cv2 as cv
import numpy as np 

def nothing(x):
	pass

img = np.zeros((400,400,3), np.uint8)
cv.namedWindow('Image')

# CREATE TRACKBAR

cv.createTrackbar('R', 'Image', 0,255, nothing)
cv.createTrackbar('G', 'Image', 0,255, nothing)
cv.createTrackbar('B', 'Image', 0,255, nothing)

# CREATE SWITCH ON-OFF
switch = '0 : OFF` \n 1 : ON'
cv.createTrackbar(switch, 'Image', 0, 1, nothing)

while(1):
	cv.imshow('Image', img)
	if cv.waitKey(1) & 0xFF == ord('q'):
		break

	# GET CURRENT POSITION OF 4 TRACKBARS
	r = cv.getTrackbarPos('R', 'Image')
	g = cv.getTrackbarPos('G', 'Image')
	b = cv.getTrackbarPos('B', 'Image')
	s = cv.getTrackbarPos(switch, 'Image')

	if s == 0:
		img[:] = 0
	else:
		img[:] = [b,g,r]

cv.destroyAllWindows()
