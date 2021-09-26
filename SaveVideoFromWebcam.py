import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

# DEFINE THE CODEC and CREATE VideoWriter Obeject
fourcc = cv.VideoWriter_fourcc(*'XVID')
outputVideo = cv.VideoWriter('outputHIGH.avi', fourcc, 60.0, (640, 480))


while cap.isOpened():
	ret , frame = cap.read()
	if not ret:
		print('cannot receive the frame, exiting')
		break

	frame = cv.flip(frame, 1)


	# WRITE THE FLIPPED FRAME
	outputVideo.write(frame)

	cv.imshow('Video', frame)
	if cv.waitKey(1) == ord('q'):
		break

cap.release()
cv.destroyAllWindows()