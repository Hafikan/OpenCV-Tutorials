# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2 as cv

data = cv.imread("imges/dog.jpg")
h, w, ch = data.shape

for row in range(h):
    for col in range(w):
        b, g, r = data[row, col]
        b =  - b
        g =  - g
        r = - r
        
        data[row, col] = [b, g, r]
cv.imshow("Image", data)

cv.waitKey(0)
cv.destroyAllWindows()