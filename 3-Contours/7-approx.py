import cv2 as cv
import numpy as np

data = cv.imread("./greenHat.jpg")
data = cv.medianBlur(data,5)
dataHsv=cv.cvtColor(data,cv.COLOR_BGR2HSV)


lower_color = np.array([59,13,0])
upper_color = np.array([72,255,169])

mask = cv.inRange(dataHsv, lower_color,upper_color)
mask = cv.dilate(mask,(3,3),iterations=3)

contour, _ = cv.findContours(mask,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

for i in range(len(contour)):

    cv.drawContours(data,contour,i,(0,0,255),4)

cv.imshow("Original",data)
cv.imshow("Hsv",dataHsv)
cv.imshow("Mask",mask)
cv.imwrite("./greenHatDetect.jpg",data)
cv.waitKey(0)
cv.destroyAllWindows()