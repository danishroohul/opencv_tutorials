# To import opencv
import cv2

#To read an image in matrix format
img = cv2.imread('lena.jpg',0) # 0 = Grayscale, 1 = Colour, -1 = As it is

#To print the matrix
print(img)

#To display the image
cv2.imshow('Image',img)
k = cv2.waitKey(0)  # 0 = Stay forever, 5000 = 5 seconds

if k == 27: #Close the window without saving when escape is pressed
    cv2.destroyAllWindows()
elif k == ord('s'): #Save image when s is pressed
    #Save the image
    cv2.imwrite('lena_copy.png',img)
    cv2.destroyAllWindows()
