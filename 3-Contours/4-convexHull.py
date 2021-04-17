# -*- coding: utf-8 -*-

import cv2 as  cv
import numpy as np


img = cv.imread("images/map.jpg")
bg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur = cv.blur(bg,(3,3))
_,thres = cv.threshold(blur,200,255,cv.THRESH_BINARY)
contours,_ = cv.findContours(thres, cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
hull =  []

for i in range(len(contours)):
    hull.append(cv.convexHull(contours[i],False))
for i in range(len(contours)):
    cv.drawContours(img, contours,i,(0,255,0),3,8)
    cv.drawContours(img, hull,i,(0,0,255),4,8)
cv.imshow("image",img)
cv.waitKey(0)
cv.destroyAllWindows()