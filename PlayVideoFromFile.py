import cv2 as cv


cap = cv.VideoCapture('outputHIGH.avi')

if cap.isOpened() == False:
	print('Error opening video file')
else:
	fps = cap.get(5)

while cap.isOpened():
	ret , frame  = cap.read()

	if ret == True:
		cv.putText(frame, f"{fps} fps ", (50,50),cv.FONT_ITALIC, 1, (0,0,255), 2, cv.LINE_AA)
		cv.imshow('Video', frame)
		k = cv.waitKey(20)
		if k == 113:
			break
	else:
		break

cap.release()
cv.destroyAllWindows()