 # -*- coding: utf-8 -*-

import cv2 as  cv
import numpy as np
 
img = cv.imread("Images/rect.jpg") #görüntü dosyasını çekme
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV) #rgb den hsv ye dönüşüm
hsv = cv.medianBlur(hsv,45) #blurlama, görüntü, eşik değeri

l_blue = np.array([85,45,6],np.uint8)#hsv uzayında mavi renginin lower kodları
u_blue = np.array([135,255,255],np.uint8)#hsv uzayında mavi renginin upper kodları
mask = cv.inRange(hsv,l_blue,u_blue) #görüntü,  hsv lower kodları, hsv upper kodları 


kernel = np.ones((3,5),np.uint8)#erode için kernel değeri, zeros for dilate, ones for erode
mask = cv.erode(mask,kernel,iterations=4)#görüntü, kernel değeri, tekrarlama değeri
conts, _ = cv.findContours(mask,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE) # kenarları bulma, görüntü ve methodlar

for i in range(len(conts)):#resim üzerine yazma
    cv.drawContours(img,conts,-1,(0,0,255),4)

m  = cv.moments(mask) #görüntü değeri

x = int(m["m10"]/m["m00"]) # x koordinatları için m içinden değerler çektik
y = int(m["m01"]/m["m00"]) # y koordinatları için m içinden değerler çektikcd ..

cv.circle(img,(x,y),5,(255,0,255),-1)


cv.imshow("mask",mask)
cv.imshow("image",img)


cv.waitKey(0)
cv.destroyAllWindows()

