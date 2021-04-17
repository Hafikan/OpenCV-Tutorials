import cv2 as cv
img = cv.imread("images/poly.png")
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

_,thres= cv.threshold(gray,127,255,cv.THRESH_BINARY)

contours,_ = cv.findContours(thres,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
#print(contours[0])#sadece üçgenin kenarlarını belirliyor, pencerenin çevresi dahil değil

moments = cv.moments(contours[0])
print(moments["m00"]) #alan hesabı

perimeter = cv.arcLength(contours[0],True)
print(perimeter)

