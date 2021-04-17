from matplotlib import pyplot as mp
import numpy as np
import cv2 as cv

img = cv.imread("imges/cards.jpg",0)


mp.hist(img.ravel(),256,[0,256]) 
mp.show()

cv.waitKey(0)
cv.destroyAllWindows()