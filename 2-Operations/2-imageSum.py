import cv2 as cv
import numpy as np
pic1 = np.zeros((512,512,3), dtype=np.uint8)+255
cv.circle(pic1,(256,256),50,(255,0,0),-1)

pic2 = np.zeros((512,512,3), dtype=np.uint8)+255
cv.rectangle(pic2,(206,206),(300,300),(0,0,255),-1)

cv.imshow("Daire",pic1)
cv.imshow("Kare",pic2)

add = cv.add(pic1,pic2)
cv.imshow("Add",add)

w = cv.addWeighted(pic1,0.3,pic2,0.5,1)
cv.imshow("Weighted",w)

cv.waitKey(0)
cv.destroyAllWindows()

