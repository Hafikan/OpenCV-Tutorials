import numpy as np
import cv2 as cv

img = cv.imread("images/corner.jpg")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray = np.float32(gray)

corners = cv.goodFeaturesToTrack(gray,img.shape[0],0.01,img.shape[0]/200)#src, corner count, scale, corner distances
for corner in corners:
    x,y = corner.ravel()
    cv.circle(img,(x,y),3,(0,0,255),-1)


cv.imshow("Corners",img)
cv.waitKey(0)
cv.destroyAllWindows()