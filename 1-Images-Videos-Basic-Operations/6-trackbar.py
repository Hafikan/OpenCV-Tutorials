import cv2 as cv
import numpy as np 

def nothing(x):
    pass

img = np.zeros((512,512,3),dtype=np.uint8)
cv.namedWindow("TrackBar")

cv.createTrackbar("R","TrackBar",0,255,nothing) #trackbar-name, window name, min - max values, func
cv.createTrackbar("G","TrackBar",0,255,nothing)
cv.createTrackbar("B","TrackBar",0,255,nothing)
switch ="0=>off,1=>on"
cv.createTrackbar(switch,"TrackBar",0,1,nothing)

while True:
    cv.imshow("TrackBar",img)
    
    if cv.waitKey(1) & 0xFF == ord("q"):
        break

    r = cv.getTrackbarPos("R","TrackBar")#trackbar-name, window-name
    g = cv.getTrackbarPos("G","TrackBar")
    b = cv.getTrackbarPos("B","TrackBar")
    s = cv.getTrackbarPos(switch,"TrackBar")
    
    if s == 0:
        img[:] == [0,0,0]
    
    if s ==1 :
        img[:]=[b,g,r]
cv.waitKey(0)
cv.destroyAllWindows()