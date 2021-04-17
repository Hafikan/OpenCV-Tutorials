import cv2 as cv 
import numpy as np

data = cv.imread("images/sudoku.jpg",0)
ret,threshold = cv.threshold(data,125,255,cv.THRESH_BINARY) #image, min thresh, max thresh, thres method
ret,threshold = cv.threshold(data,125,255,cv.THRESH_BINARY_INV)
ret,threshold = cv.threshold(data,125,255,cv.THRESH_TRUNC)
ret,threshold = cv.threshold(data,125,255,cv.THRESH_TOZERO)
ret,threshold = cv.threshold(data,125,255,cv.THRESH_TOZERO_INV)
ret,threshold = cv.threshold(data,125,255,cv.THRESH_BINARY + cv.THRESH_OTSU)
#cv.imshow("Thres",threshold)

adapThresholdm= cv.adaptiveThreshold(data,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,7,2)
#cv.imshow("Adaptive-Mean",adapThresholdm)

adapThresholdc = cv.adaptiveThreshold(data,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,19,2.3)
cv.imshow("Adaptive-Gaus",adapThresholdc)

cv.waitKey(0)
cv.destroyAllWindows()

