import cv2 as cv 
import numpy as np 

draw= False
#---------------------------
pic = np.ones((512,512,3), dtype=np.uint8)
cv.namedWindow("Paint")

#------------------------------
def nothing(x):
    pass


cv.createTrackbar("R","Paint",0,255,nothing)
cv.createTrackbar("G","Paint",0,255,nothing)
cv.createTrackbar("B","Paint",0,255,nothing)
cv.createTrackbar("S","Paint",0,10,nothing)


#--------------------------
def get_track():
    global r,b,g,s
    r = cv.getTrackbarPos("R","Paint")
    g = cv.getTrackbarPos("G","Paint")
    b = cv.getTrackbarPos("B","Paint")
    s = cv.getTrackbarPos("S","Paint")

    return (b,g,r,s)

#----------------------------
def brush(event,x,y,flag,param):
    global draw

    if event == cv.EVENT_LBUTTONDOWN:
        draw = True
    elif event == cv.EVENT_MOUSEMOVE:
        if draw == True:
            cv.circle(pic,(x,y),s,(b,g,r),-1)
    else:
        draw = False
#----------------------
while True:
    cv.imshow("Paint",pic)
    if cv.waitKey(1) & 0xFF == ord("q"):
        break 
    else:
        get_track()
        cv.setMouseCallback("Paint",brush)

cv.waitKey(0)
cv.destroyAllWindows()      