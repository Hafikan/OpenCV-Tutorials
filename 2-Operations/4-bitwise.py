import cv2 as cv
import numpy as np

pic1 = np.zeros((512,512,3),np.uint8)
pic2 = np.zeros((512,512,3),np.uint8)

pic1[:420,:255] = [255,255,255]
pic2[420:,255:]=[255,255,255]


bit1 = cv.bitwise_and(pic1,pic2)
#cv.imshow("BİT And",bit1)

bit2 = cv.bitwise_or(pic1,pic2)
#cv.imshow("Bit Or",bit2)

bit3 = cv.bitwise_xor(pic1,pic2)
#cv.imshow("Bit Xor",bit3)

bit4 = cv.bitwise_not(pic1)

cv.imshow("Bit not",bit4)

cv.waitKey(0)
cv.destroyAllWindows()