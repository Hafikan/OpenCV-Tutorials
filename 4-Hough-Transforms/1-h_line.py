import cv2 as cv
import numpy as np
pic = cv.imread("images/line.jpg")
gray = cv.cvtColor(pic, cv.COLOR_BGR2GRAY)

side = cv.Canny(gray,75,75)
line = cv.HoughLinesP(side,1, np.pi/180, 75,maxLineGap = 1000)
for i in line:
    x1,y1,x2,y2 = i[0]
    cv.line(pic,(x1,y1),(x2,y2),(0,100,250),2)
    
    
    
cv.imshow("Org",pic)
cv.waitKey(0)
cv.destroyAllWindows()

