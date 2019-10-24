import numpy as np
import cv2

#Click event function used when mouse button is clicked
def click_event(event,x,y,flags,param):

    #For left button click
    if event == cv2.EVENT_LBUTTONDOWN:

        #Append x,y into the list
        points.append((x,y))

        #if points are more than 2, connect them with a line
        if len(points) >= 2:
            #Connect the last 2 points
            cv2.line(img,points[-1],points[-2],(255,0,0),10)
        cv2.imshow("image",img)

img = cv2.imread("lena.jpg",1)
cv2.imshow("image",img)

#Create an empty list for storing points
points = []

#setMouseCallback gets triggered when ever mouse click event occurs
cv2.setMouseCallback("image",click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
