# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = np.zeros((512,512,3),np.uint8)
#change color =>>  img[:]=125,125,87


#line draw
cv.line(img,(0,0),(300,200),(125,125,12),2)#src,start-point,end-point,color, thickness, line-type

#rect draw
cv.rectangle(img,(0,10),(30,499),(122,122,122),2)#src,start-point,end-point,color, thickness, line-type

#circle draw
cv.circle(img,(400,200), 40,(20,20,125),4)#src,center-point,radius,color, thickness, line-type

#Text draw
cv.putText(img,"OPEN CV",(0,311),cv.FONT_HERSHEY_COMPLEX,10,(125,125,12),4)#src,text,start-point,font,font-size,color,font-weight

#poly line draw
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int64)
pts = pts.reshape((-1,1,2))
cv.polylines(img,[pts],True,(0,0,255),) #image,point,close/open,color

#ellipse draw
cv.ellipse(img,(256,256),(100,200),0,0,290,255,-1)#image, center Coord, axes, angle, start angle, end angle,color, thickness
cv.imshow("Image",img)

cv.waitKey(0)
cv.destroyAllWindows()

