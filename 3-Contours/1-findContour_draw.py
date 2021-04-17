import cv2 as cv

img = cv.imread("images/contour.png")
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

_,thresh = cv.threshold(gray,127,255,cv.THRESH_BINARY)

contours,_ = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE,)

cv.drawContours(img, contours,0,(0,255,0),1) #-1 tüm köşeleri buluyor, 0 en dıştakini buluyor yani pencerenin kenarlarını

cv.imshow("Contours",img)
cv.waitKey(0)
cv.destroyAllWindows()