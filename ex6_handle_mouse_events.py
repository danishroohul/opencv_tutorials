import numpy as np
import cv2

#Extract list of events from cv2 library
events = [i for i in dir(cv2) if "EVENT" in i]
print(events)

#Click event function used when mouse button is clicked
def click_event(event,x,y,flags,param):

    #For left button click
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,", ",y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = "*"+str(x) + ", " + str(y)
        cv2.putText(img,strXY,(x,y),font,0.5,(255,255,0),2)
        cv2.imshow("image",img)

    #For right button click
    if event == cv2.EVENT_RBUTTONDOWN:
        #0 = blue channel, 1 =  green channel and 2 = red channel (BGR format)
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = "*"+str(blue) + ", " + str(green) + ", " + str(red)
        cv2.putText(img,strBGR,(x,y),font,0.5,(0,255,255),2)
        cv2.imshow("image",img)

img = cv2.imread("lena.jpg",1)
cv2.imshow("image",img)

#setMouseCallback gets triggered when ever mouse click event occurs
cv2.setMouseCallback("image",click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
