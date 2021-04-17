import cv2 as cv 
import numpy as np 
import imutils


def nothing(x):
    pass

img = cv.imread("paper2.png")
img = imutils.resize(img,width=640,height=480)




while True:
    succes = True
    frame = img.copy()

    if succes == False:
        break
    
    else:
    

        frameBlur = cv.medianBlur(frame,5)
        frameGray = cv.cvtColor(frameBlur,cv.COLOR_BGR2GRAY)
        ret,frameThresh = cv.threshold(frameGray,160,255,cv.THRESH_BINARY)
        kernel = np.ones((5,5))
        canny = cv.Canny(frameThresh,100,150)
        frameDil = cv.dilate(canny,kernel,iterations=2)
        

        imgContours = frame.copy()
        contours, hiearch = cv.findContours(frameDil,cv.CHAIN_APPROX_SIMPLE,cv.RETR_TREE)
        cv.drawContours(imgContours,contours,-1,(0,255,255),5)
        
        c = max(contours,key = cv.contourArea)
        
        x,y,w,h = cv.boundingRect(c)
        cv.rectangle(frame,(x,y),(x+w,y+h),(70,200,50),2)
        pts1 = np.float32([[x,y],[x+w,y],[x,y+h],[x+w,y+h]])
        pts2 = np.float32([[0,0],[640,0],[0,480],[640,480]])
        matrix = cv.getPerspectiveTransform(pts1, pts2)
        imgWarpColored = cv.warpPerspective(frame, matrix, (640, 480))

        #REMOVE 20 PIXELS FORM EACH SIDE
        imgWarpColored=imgWarpColored[20:imgWarpColored.shape[0] - 20, 20:imgWarpColored.shape[1] - 20]
        imgWarpColored = cv.resize(imgWarpColored,(640,480))

        cv.imshow("img",img)
        cv.imshow("dilate",frameDil)
        cv.imshow("contours",frame)
        cv.imshow("warp",imgWarpColored)    

        dst = cv.detailEnhance(imgWarpColored,15, 1.5)    
        cv.imshow("dst",imgWarpColored)

        


        if cv.waitKey(27) & 0xFF == ord("q"):
            break



cv.destroyAllWindows()
        