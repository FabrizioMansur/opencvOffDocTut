import cv2 as cv 
import numpy as np

events = [i for i in dir(cv) if 'EVENT' in i]
print(events)

drawing = False # TRUE IF THE MOUSE IS PRESSED

mode = True # IF TRUE DRAW A RECTANGLE, press M to TOGGLE to curve

ix, iy = -1, -1

# mouse call back function

def draw_circle(event, x, y, flags, param):
	global ix, iy, drawing , mode

	if event == cv.EVENT_LBUTTONDOWN:
		drawing = True
		ix,iy  = x,y

	elif event == cv.EVENT_MOUSEMOVE:
		if drawing == True:
			if mode == True:
				cv.rectangle(img, (ix,iy), (x,y), (0,255,0), -1)
			else:
				cv.circle(img, (ix,iy), 100, (0,0,255), -1)

	elif event == cv.EVENT_LBUTTONUP:
		drawing == False
		if mode == True:
			cv.rectangle(img, (ix,iy), (x,y), (0,255,0), -1)
		else:
				cv.circle(img, (ix,iy), 100, (0,0,255), -1)

# Create a window

img = np.zeros((400,500,3), np.uint8)
cv.namedWindow('Image')
cv.setMouseCallback('Image', draw_circle)

while(1):
	cv.imshow('Image', img)
	k = cv.waitKey(1) & 0xFF
	if k == ord('m'):
		mode = not mode
	elif k == ord('q'):
		break

cv.destroyAllWindows()
