import cv2

cam = cv2.VideoCapture(0)
face_casc = cv2.CascadeClassifier("./XML/frontalface.xml")#cascade dosyasını dahil etme


while True:
    succs, frame = cam.read()
    picG=  cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face = face_casc.detectMultiScale(picG,1.1,5) #yüz tespiti için kullandığımız fonksiyon

    for (x,y,w,h) in face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        
    cv2.imshow("Faces",frame)
    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

cv2.waitKey(0)
cv2.destroyAllWindows()

