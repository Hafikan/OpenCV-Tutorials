import cv2 as cv


img = cv.imread("images/contour.png")
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
_,thres = cv.threshold(gray,127,255,cv.THRESH_BINARY)
m  = cv.moments(thres)

x = int(m["m10"]/m["m00"])
y = int(m["m01"]/m["m00"])

cv.circle(img,(x,y),5,(255,0,255),-1)
cv.imshow("İmage",img)
cv.waitKey(0)
cv.destroyAllWindows()