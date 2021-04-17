import cv2 
import numpy as np
 
img = cv2.imread('imges/cards.jpg') 
blue, green, red = cv2.split(img) 

canvas = np.zeros(green.shape, np.uint8)

blue = cv2.merge((blue,canvas, canvas))
green = cv2.merge((canvas,green,canvas))
red = cv2.merge((canvas,canvas,red))
cv2.imshow("blue",blue)
cv2.imshow("green",green)
cv2.imshow("red",red)




cv2.waitKey(0)
cv2.destroyAllWindows()