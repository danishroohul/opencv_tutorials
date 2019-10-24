import cv2

#Capture video from inbuilt camera by giving 0
#Or give the video name with its extension
cap = cv2.VideoCapture(0)

#Get the video frame width and height
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#Set the video frame width and height to desired values
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 100)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 100)

#Print the frame width and height values
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#Run the loop when video is available from camera
while cap.isOpened():
    #ret = Boolean value which tells frame is available or not
    #frame = Image frame from the camera
    ret,frame = cap.read()
    if ret == True:
        #Convert image to gray
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',gray)

        #If q is pressed, exit the video displaying
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

#Release the cap opject
cap.release()

#Close all windows of camera
cv2.destroyAllWindows()
