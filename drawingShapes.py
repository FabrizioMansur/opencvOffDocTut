import cv2 as cv
import numpy as np

# CREATE A BLACK IMAGE
tela = np.zeros((600,600,3), np.uint8)
foto = cv.imread('pythonOpencv.png')

# DRAW A LINE pointA = (x1,y1) pointB = (x2,y2)
cv.line(tela, (50,50), (550,550), (255,0,0), 5)
cv.line(tela, (550,50), (50,550), (0,255,0), 5)
cv.line(foto, (29,39), (358,39), (0,0,255), 5)
cv.line(foto, (360,40), (360,367), (0,255,0),5)

# DRAW A CIRCLE (x,y) radius color thickness
cv.circle(tela, (300,300), 100, (0,255,255),3)
cv.circle(foto, (696,178), 142, (255,255,0), 3, cv.LINE_AA)

# DRAW A RECTANGLE
cv.rectangle(tela, (49,49), (551,551), (150,150,150), 3, cv.LINE_8)
cv.rectangle(foto, (29,39), (840,374), (255,0,255), 3, cv.LINE_8)

# HORIZONTAL ELLIPSE (center), (mayor axis, min axis)
cv.ellipse(tela, (300,300), (150,50), 0,0,360, (150,0,150), 3)

#VERTICAL ELLIPSE
cv.ellipse(tela, (300,300), (150,50), 90,0,360, (255,255,255), 3)

# DIAGONAL ELLIPSE
cv.ellipse(tela, (300,300), (150,50), 45,0,360, (25,50,75), 3)
cv.ellipse(tela, (300,300), (150,50), 135,0,360, (75,50,25), 3)

# POLIGON
points = np.array([[50,50], [100,50], [100,100], [50,100]], np.int32)
#points = points.reshape((-1,1,2))
cv.polylines(tela,[points],True, (0,255,255),5)

# WRITE TEXT
cv.putText(foto, 'OPENCV', (569,300), cv.FONT_ITALIC, 1, (0,0,255), 2, cv.LINE_AA)
cv.putText(tela, 'ATOM', (265,46),cv.FONT_ITALIC, 1, (255,255,255), 2, cv.LINE_AA)


cv.imshow('Tela Nera', tela)
cv.imshow('foto', foto)
cv.waitKey(0)