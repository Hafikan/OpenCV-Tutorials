import numpy as np 
import cv2 as cv 

img = cv.imread("images/test2.png",)
row,col = img.shape[0:2]
#--------İmage Scroll------------
Margin = np.float32([[1,0,105],[0,1,105]])

dst = cv.warpAffine(img,Margin,(col,row))
cv.imshow("Dst",dst)


#--------İmage Flip-----------
rotate = cv.getRotationMatrix2D((col/3,row/3),125,5)
dst = cv.warpAffine(img,rotate,(col,row))

cv.imshow("Rotate",dst)





cv.waitKey(0)
cv.destroyAllWindows()