import numpy as np 
import cv2 as cv 

data = cv.imread("imges/dog.jpg")
dataBlue = data.copy()
dataRed = data.copy()
dataGreen = data.copy()

cv.imshow("data1",data)
r,g,b = cv.split(data)

w,h =data.shape[0:2]
for i in range(w):
    for j in range(h):
        
        dataBlue[i,j,:] = (b[i,j],0,0)
        dataRed[i,j,:] = (0,0,r[i,j])
        dataGreen[i,j,:] = (0,g[i,j],0)


    

cv.imshow("dataBlue",dataBlue)
cv.imshow("dataRed",dataRed)
cv.imshow("dataGreen",dataGreen)
cv.waitKey(0)
cv.destroyAllWindows()