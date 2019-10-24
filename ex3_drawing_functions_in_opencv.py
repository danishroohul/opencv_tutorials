import numpy as np
import cv2

#To create a black image using numpy
img = np.zeros([512,512,3],np.uint8)

#To read an image from files in colour mode
#img = cv2.imread('lena.jpg',1)

#To draw a line use cv2.line Function
#First arg = file name
#Second arg = start point
#Third arg = end point
#Fourth arg = colour of the line
#Fifth arg = thickness of the line
img = cv2.line(img,(0,0),(255,255),(255,0,0),10)

#To draw a line use cv2.arrowedLine Function
#First arg = file name
#Second arg = start point
#Third arg = end point
#Fourth arg = colour of the line
#Fifth arg = thickness of the line
img = cv2.arrowedLine(img,(0,255),(255,255), (0,255,0),10)

#To draw a circle use cv2.circle Function
#First arg = file name
#Second arg = center point
#Third arg = radius
#Fourth arg = colour of the line
#Fifth arg = thickness of the line
img = cv2.circle(img, (255,255), 100, (255,255,255), 10)

#To draw a rectangle use cv2.rectangle Function
#First arg = file name
#Second arg = start point - top left corner point
#Third arg = end point - bottom right corner point
#Fourth arg = colour of the line
#Fifth arg = thickness of the line
img = cv2.rectangle(img,(384,0), (510,128), (0,0,255), 10)

#Font used for inserting the text
font = cv2.FONT_HERSHEY_COMPLEX

#To insert text on the image use cv2.putText Function
#First arg = file name
#Second arg = Text to be printed
#Third arg = start point
#Fourth arg = font of the text
#Fifth arg = size of the Text
#Sixth arg = colour of the text
#Seventh arg = Thickness of the text
#Eight arg = Line type
img = cv2.putText(img,"Yo, hola!!", (10,500), font, 2, (100,120,130), 8, cv2.LINE_AA)


cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
