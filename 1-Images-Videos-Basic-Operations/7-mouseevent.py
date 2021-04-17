# -*- coding: utf-8 -*-
import cv2 as cv

def click_event(event,x,y,flag,param):
    if event == cv.EVENT_FLAG_LBUTTON:#left click
        strXY = str(x)+" "+str(y)
        font=cv.FONT_HERSHEY_SIMPLEX
        cv.putText(img, strXY, (x,y), font,.75, (125,125,125))
        cv.imshow("İmage",img)
        
        
img = cv.imread("imges/coins1.jpg")
cv.imshow("İmage",img)
cv.setMouseCallback("İmage", click_event) #image, event function

cv.waitKey(0)
cv.destroyAllWindows()