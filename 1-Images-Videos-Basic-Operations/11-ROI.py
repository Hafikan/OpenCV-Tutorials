import cv2 as cv
import numpy as np

data = cv.imread("imges/dog.jpg")

cv.namedWindow("Image", cv.WINDOW_AUTOSIZE)
cv.imshow("Image", data)
h, w = data.shape[:2]

ry = h//3
rx = w//3
roi = data[ry-100:ry+100,rx-100:rx+100,:]

cv.imshow("roi", roi)

copy = np.copy(roi)
copy [:,:,0] = 0
cv.imshow("copy",copy)


cv.waitKey(0)
cv.destroyAllWindows()