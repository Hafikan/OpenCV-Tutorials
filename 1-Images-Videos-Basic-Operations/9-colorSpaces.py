import cv2 as cv

#img = cv.imread("images/klon.jpg")

#imgH = cv.cvtColor(img,cv.COLOR_BGR2HSV) convert BGR to HSV
#imgG = cv.cvtColor(img, cv.COLOR_BGR2GRAY) convert BGR to Gray


#cv.imshow("İmage",img)
#cv.imshow("İmageH",imgH)
#cv.imshow("İmageG",imgG)

video = cv.VideoCapture(0)

while True:

    success, frame = video.read()

    frame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

    if success == False:
        break
    
    else:
        cv.imshow("Gri Film",frame)
    if cv.waitKey(25) & 0xFF == ord("q"):
        break
    
video.release()
cv.waitKey(0)
cv.destroyAllWindows()