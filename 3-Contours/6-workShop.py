import numpy as np
import cv2 as cv

cam = cv.VideoCapture(0)

def nothing(x):
    pass

cv.namedWindow("TrackBar")
cv.resizeWindow("TrackBar",640,480)

cv.createTrackbar("Lower H", "TrackBar",0,180,nothing)
cv.createTrackbar("Lower S", "TrackBar",0,255,nothing)
cv.createTrackbar("Lower V", "TrackBar",0,255,nothing)

cv.createTrackbar("Upper H", "TrackBar",0,180,nothing)
cv.createTrackbar("Upper S", "TrackBar",0,255,nothing)
cv.createTrackbar("Upper V", "TrackBar",0,255,nothing)

#when started
cv.setTrackbarPos("Upper H","TrackBar",180)
cv.setTrackbarPos("Upper S","TrackBar",255)
cv.setTrackbarPos("Upper V","TrackBar",255)

while True:
    success, frame = cam.read()

    frameHsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)

    l_h = cv.getTrackbarPos("Lower H","TrackBar")
    l_s = cv.getTrackbarPos("Lower S","TrackBar")
    l_v = cv.getTrackbarPos("Lower V","TrackBar")

    u_h = cv.getTrackbarPos("Upper H", "TrackBar")
    u_s = cv.getTrackbarPos("Upper S", "TrackBar")
    u_v = cv.getTrackbarPos("Upper V", "TrackBar")

    lower_color = np.array([l_h,l_s,l_v,])
    upper_color = np.array([u_h,u_s,u_v,])

    mask = cv.inRange(frameHsv, lower_color,upper_color)
    mask =  cv.dilate(mask,(5,5),iterations=2)
    mask = cv.medianBlur(mask,5)
    bit = cv.bitwise_and(frame,frame,mask=mask)

    c,h = cv.findContours(mask,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

    for cnt in range(len(c)):
        area = cv.contourArea(c[cnt])
        if area < 320:
            continue
        rect = cv.minAreaRect(c[cnt])
        cx, cy = rect[0]
        box = cv.boxPoints(rect)
        box = np.int0(box)
        cv.drawContours(frame,[box],0,(0,0,255),2)
        cv.circle(frame, (np.int32(cx), np.int32(cy)), 2, (255, 0, 0), 2, 8, 0)
        M = cv.moments(box)
        cv.putText(frame,str(M["m00"]),(50,50,),cv.FONT_HERSHEY_COMPLEX,2,(0,0,255),2)
        #l-blue = 28,52,92
        #u-blue = 180,255,255


    cv.imshow("Orginal",frame)
    cv.imshow("Hsv",mask)
    cv.imshow("bitwise",bit)
    if cv.waitKey(25) & 0xFF == ord("q"):
        break

cv.waitKey(0)
cv.destroyAllWindows()