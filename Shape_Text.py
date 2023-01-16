import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8) # image size and 3 to add color function
# print(img)
# img[:]= 255,0,0  whole image turn to blue

# cv2.line(img,(0,0),(300,300),(0,255,0),3)  # coordinate for line, color and thickness
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3) # width and height from img shape
cv2.rectangle(img,(0,0),(250,350),(0,0,255),cv2.FILLED) # thickness or filled the shape with color
cv2.circle(img,(400,50),30,(255,255,0),5)
cv2.putText(img," OPENCV ",(300,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),3) # text, position, font scale and thickness, color



cv2.imshow("Image",img)
cv2.waitKey(0)