# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = cv.imread("images/test.png")

imgBlurC=cv.GaussianBlur(img, (7,3), 15)
#cv.imshow("Gaussian",imgBlurC)

imgBlurM = cv.medianBlur(img,5)
#cv.imshow("Median",imgBlurM)

imgBlur = cv.blur(img,(5,5))
#cv.imshow("Blur",imgBlur)

imgBil= cv.bilateralFilter(img,15,75,75)
#cv.imshow("Bilateral",imgBil)

imgCanny=cv.Canny(img,100,100)
#cv.imshow("Canny",imgCanny)

kernel= np.ones((5,5),np.uint8)

imgDilation = cv.dilate(imgCanny,kernel,iterations=1)
#cv.imshow("Dilation",imgDilation)

imgEroded = cv.erode(imgDilation,kernel,iterations=1)
#cv.imshow("Eroded",imgEroded)

imgOpenin = cv.morphologyEx(imgEroded, cv.MORPH_OPEN, kernel)
#cv.imshow("Opening",imgOpenin)

imgClose = cv.morphologyEx(imgOpenin, cv.MORPH_CLOSE, kernel)
#cv.imshow("Close",imgClose)

imgGradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
#cv.imshow("Gradient",imgGradient)


cv.waitKey(0)
cv.destroyAllWindows()