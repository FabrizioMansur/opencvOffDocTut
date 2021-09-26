import cv2 as cv
import numpy as np

events = [i for i in dir(cv) if 'EVENT' in i]
print(events)

ix, iy = -1, -1

# MOUSE CALL BACK FUNCTION

def draw_circle(event, x, y, flags, param):
	if event == cv.EVENT_LBUTTONDBLCLK:
		#cv.circle(img, (x,y), 100, (255,0,0), -1)
		cv.rectangle(img, (ix,iy), (x,y), (0,255,0), -1)

# CREATE A BLACK IMAGE, A WINDOW, and bind the Function to the window
img = np.zeros((500,500,3), np.uint8)

cv.namedWindow('Image')
cv.setMouseCallback('Image', draw_circle)

while(1):
	cv.imshow('Image', img)
	if cv.waitKey(1) == ord('q'):
		break

cv.destroyAllWindows()