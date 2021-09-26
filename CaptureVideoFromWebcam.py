import cv2 as cv
import numpy as np
import time
import datetime

cap = cv.VideoCapture(0)

date_time = str(datetime.datetime.now())

prev_frame_time = 0
new_frame_time = 0

if not cap.isOpened():
	print('cannot open the camera')

while True:
	# CAP FRAME BY FRAME ( if the frmae is opened correctly ret is true)
	ret, frame = cap.read()

	if not ret:
		print('cannot receive the frame, exiting')
		break

	# OPERATION ON THE FRAME
	#gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
	new_frame_time = time.time()
	fps = 1/(new_frame_time-prev_frame_time)
	prev_frame_time = new_frame_time
	fps = int(fps)

	frame = cv.flip(frame, 1)
	frame_width = int(cap.get(3))
	frame_height = int(cap.get(4))

	cv.putText(frame, f"{fps} fps {frame_width} width {frame_height} height ", (50,50),cv.FONT_ITALIC, 1, (0,0,255), 2, cv.LINE_AA)
	cv.putText(frame, f"today {date_time}", (20,450),cv.FONT_ITALIC, 1, (0,255,255), 2, cv.LINE_AA)
	cv.circle(frame,(320,240), 100,(255,255,0), 3, cv.LINE_AA)

	# DISPLAY THE RESULTING FRAME
	cv.imshow('GRAY FRAME', frame)

	if cv.waitKey(1) == ord('q'):
		break

# WHEN EVERYTHING IS READY
cap.release()
cv.destroyAllWindows()
