# -*- coding: utf-8 -*-

import cv2 as cv
import numpy as np

data = cv.imread("images/test2.png")

h, w = data.shape[:2]

#Laplacian

edge = cv.Laplacian(data, cv.CV_32F)
#cv.imshow("laplacian", edge)

dst = cv.convertScaleAbs(edge)

result = np.zeros([h, w*2, 3], dtype=data.dtype)
result[0:h,0:w,:] = data
result[0:h,w:2*w,:] = dst

cv.imshow("result", result)
cv.imshow("output",dst)

cv.waitKey(0)
cv.destroyAllWindows()# -*- coding: utf-8 -*-


#Canny
canny = cv.Canny(data,50,100,apertureSize=4,L2gradient=True)

cv.imshow("Canny",canny)


#sobel

sobelx = cv. Sobel (data, cv.CV_64F, 1 , 0, ksize = 5) # x
sobely = cv. Sobel (data, cv.CV_64F, 0, 1 , ksize = 5) # y
cv.imshow("X",sobelx)
cv.imshow("Y",sobely)