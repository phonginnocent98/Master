# Resize the image
import cv2
import numpy as np

img = cv2.imread("Resources/pokemon.png")
print(img.shape)


imgResize = cv2.resize(img,(300,200))
print(imgResize.shape)  # show the size of image width + height

imgCropped = img[0:200,20:100] # height + width

cv2.imshow("Image",img)
cv2.imshow("Iamge Resize",imgResize)
cv2.imshow("Iamge Cropped",imgCropped)

cv2.waitKey(0)