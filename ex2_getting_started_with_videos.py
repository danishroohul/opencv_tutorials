#Import opencv
import cv2

#Capture video from inbuilt camera by giving 0
#Or give the video name with its extension
cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture('vid.webm');

#fourcc is the video codec, basically type of video
fourcc = cv2.VideoWriter_fourcc(*'XVID')

#VideoWriter class to save the video with a file name
#20.0 is the frames per second
#640,480 is the video size
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

#Loop to collect frames from the camera
#cap.isOpened() = returns boolean value if the video from camera or file is available
print(cap.isOpened())
while cap.isOpened():
    #ret = Boolean value which tells frame is available or not
    #frame = Image frame from the camera
    ret, frame = cap.read()

    if ret == True:

        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        #Optional line if we need to convert colour image to gray scale
        #cvtColor is function used to convert image formats
        #Camera images are by default in BGR format, so BGR2GRAY
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        out.write(frame)

        #Function used in loop gives us a video
        cv2.imshow('Frame', gray)

        #When the key received is q, then exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

#Release the VideoCapture object
cap.release()

out.release()
#Close the window
cv2.destroyAllWindows()
