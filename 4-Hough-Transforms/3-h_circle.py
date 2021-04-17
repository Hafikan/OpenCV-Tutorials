import cv2 as cv
import numpy as np
pic = cv.imread("images/coins.jpg")

gray = cv.cvtColor(pic,cv.COLOR_BGR2GRAY)
gray = cv.medianBlur(gray,7)
gray = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,1)
kern = np.ones((3,5),dtype = np.uint8)


circles = cv.HoughCircles(gray,cv.HOUGH_GRADIENT, 1.25,pic.shape[0]/4.28,param1=45,param2=120,minRadius=10,maxRadius=100)

if circles is not None:
    circles = np.round(circles[0,:]).astype("int")

    for (x,y,r) in circles:
        cv.circle(pic,(x,y),r,(0,0,255),4)


cv.imshow("org",pic)

cv.waitKey(0)
cv.destroyAllWindows()