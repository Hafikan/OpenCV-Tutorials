# -*- coding: utf-8 -*-
import cv2 as cv

img = cv.imread("imges/cards.jpg")
print(img.shape)# height,width,rgb
imgResize=cv.resize(img,(720,540))#  image, widh, height, inter

#cv.imshow("Resize İmage",imgResize)


imgCropped = img[0:720,0:540]# height, width
cv.imshow("Cropped İmage",imgCropped)

#Aspect radio, save write-height rate
def aspectRadio(image, width=None,height=None,inter=cv.INTER_AREA):
    newSize =None
    (h,w) = image.shape[:2]

    if width is None:
        r=height/float(h)
        newSize=(int(w*r),height)
    elif width is None and height is None:
        return image

    else:
        r = width(float(w))
        newSize = (width,int(h*r))


    return cv.resize(image,newSize)
image2= aspectRadio(img, width=None,height=1080,inter=cv.INTER_AREA)
cv.imwrite("imges/cards3.jpg",image2)
cv.waitKey(0)
cv.destroyAllWindows()