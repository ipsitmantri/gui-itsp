import cv2
import itertools
import numpy as np
import math
from matplotlib import pyplot as plt
image= cv2.imread("image.jpeg")#reading the query image
#image processing-
im_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
ret, im_binary = cv2.threshold(im_gray,127,255,cv2.THRESH_BINARY)
    
kernel_1 = cv2.getStructuringElement(cv2.MORPH_RECT,(2,2))
kernel_2 = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
    
img_filtered = cv2.dilate(cv2.erode(im_binary,kernel_1),kernel_2)
    
contours,hierarchy = cv2.findContours(img_filtered,1,2)
cv2.drawContours(image,contours, -1,(0,255,0),3)
no_of_stars = len(contours)
width = 500
height =700
dim = (width, height)
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
print(no_of_stars)
#gives the number of stars in the image which are further used for hashing function.

centers = []
centers_new = []
cv2.imshow('processed_image',resized)
k = cv2.waitKey(0)
if k == 95:
    cv2.destroyAllWindows()
        
