import numpy as np
import cv2

#Click event function used when mouse button is clicked
def click_event(event,x,y,flags,param):

    #For left button click
    if event == cv2.EVENT_LBUTTONDOWN:
        #Extracting colour values from that point
        #0 = blue channel, 1 =  green channel and 2 = red channel (BGR format)
        blue = img[x,y,0]
        green = img[x,y,1]
        red = img[x,y,2]

        #Create a black image to fill in colours
        my_colour = np.zeros((512,512,3),np.uint8)

        #FIll the image with the colour at that point
        my_colour[:] = [blue,green,red]
        cv2.imshow("colour",my_colour)

img = cv2.imread("lena.jpg",1)
cv2.imshow("image",img)

#Create an empty list for storing points
points = []

#setMouseCallback gets triggered when ever mouse click event occurs
cv2.setMouseCallback("image",click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
