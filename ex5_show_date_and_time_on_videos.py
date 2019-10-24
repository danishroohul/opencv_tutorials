import cv2
import datetime

#Capture video from inbuilt camera by giving 0
#Or give the video name with its extension
cap = cv2.VideoCapture(0)

#Run the loop when video is available from camera
while cap.isOpened():

    #ret = Boolean value which tells frame is available or not
    #frame = Image frame from the camera
    ret,frame = cap.read()
    if ret == True:

        #Font used for inserting the text
        font = cv2.FONT_HERSHEY_SIMPLEX

        #Get the video frame width and height
        width = str(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = str(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        #To insert text on the image use cv2.putText Function
        #Here we are inserting width and heightof the frame
        text = "Width = {}, Height = {}".format(width,height)
        cv2.putText(frame,text,(0,30),font,1,(0,255,255), 2, cv2.LINE_AA)

        #Here we are adding present time on the video
        #datetime.datetime.now() extracts present time from the computer
        datet = str(datetime.datetime.now())
        cv2.putText(frame,datet,(0,70),font,1,(0,255,255), 2, cv2.LINE_AA)

        #Display the frames
        cv2.imshow("Frame",frame)

        #Quit if q is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

#Release the cap object
cap.release()

#Close all opencv windows
cv2.destroyAllWindows()
