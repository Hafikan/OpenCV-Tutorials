import cv2
import numpy as np
img =cv2.imread("images/star.png")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thresh = cv2.threshold(gray,127,255,0)

contours,_ = cv2.findContours(thresh,2,1)
cnt = contours[0]

hull =cv2.convexHull(cnt, returnPoints = False)
defects = cv2.convexityDefects(cnt,hull)

print(defects)
for i in range(defects.shape[0]):
    start, end, far, distance = defects[i,0]
   
    start =tuple(cnt[start][0])
    end =tuple(cnt[end][0])
    far =tuple(cnt[far][0])

    cv2.line(img,start,end,(0,0,255),2)
    cv2.circle(img,far,4,(0,255,0),-1)


cv2.imshow("İmage",img)





cv2.waitKey(0)
cv2.destroyAllWindows()