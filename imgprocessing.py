from implibs import *
def processed_image(image):
    im_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) #conversion to gray scale
    ret, im_binary = cv2.threshold(im_gray,127,255,cv2.THRESH_BINARY)#converting to binary image
    
    kernel_1 = cv2.getStructuringElement(cv2.MORPH_RECT,(2,2))#morphological transformations
    kernel_2 = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
    
    img_filtered = cv2.dilate(cv2.erode(im_binary,kernel_1),kernel_2)#dilation and erosion
#making contours around each star    
    contours,hierarchy = cv2.findContours(img_filtered,1,2)
    no_of_stars = len(contours)
    
    centers = []
    centers_new = []
#finding center of each identified star.
    for i in range(no_of_stars) :
        (x,y),radius = cv2.minEnclosingCircle(contours[i])
        centers.append([x,y,radius])
    centers = sorted(centers,key=lambda point:point[2])
    for i in range(len(centers)):
        centers_new.append([centers[i][0],centers[i][1]])
    return centers_new
