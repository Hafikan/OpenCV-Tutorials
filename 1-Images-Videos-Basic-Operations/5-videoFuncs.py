import cv2 as cv

#Display Video
video = cv.VideoCapture("imges/video.mp4") #video file name, flag

while True:
    success, frame = video.read()
    
    if success == False:
        print("Video is not founded!")
        break
    else:
        
        cv.imshow("Video",frame)
    
    
    if cv.waitKey(1) == ord("q"):
        break



video.release()

#Display Video/Webcam

cam = cv.VideoCapture(0)
codec = cv.VideoWriter_fourcc("W","M","V","2")
fileName= "imges/webcam.avi"
size=(640,480)
fps =50
videoFileOutput =cv.VideoWriter(fileName,codec,fps,size) #file-name, Fourcc codec, fps, resolution

while True:
    succes ,frame = cam.read()
    
    if succes == False:
        print("Camera is not found!")
        break
        
        
    else:
        
        videoFileOutput.write(frame)
        cv.imshow("Camera",frame)

    if cv.waitKey(1) & 0xFF == ord("q"):
        break
    
cam.release()


cv.waitKey(0)
cv.destroyAllWindows()
