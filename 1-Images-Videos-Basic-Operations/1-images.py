#import modules
import numpy as np #Numpy Lib.
import cv2 as cv #OpenCV Lib


#Read the our image file
img = cv.imread("imges/cards.jpg",0)#image file name, flag
shape = img.shape

width = shape[0]
height = shape[1]


for i in range(2):
    print(img[i,0])
    
    
    
#blueİmg[100,90,0] = 247

#img.shape = 380,620,3

#img.size = 3*380*620

#blue = img[20,20,0]


#[176 225 223]

cv.waitKey(0) #for stay open
cv.destroyAllWindows() # when clicked, close all windows