import cv2
import numpy as np

img = cv2.imread("Resources/pokemon.png")

imgHor = np.hstack((img,img))
imgVer = np.vstack((img,img))  # arrange in vertical
# ko the thay doi size vaf phai cung RGB or Grey...


cv2.imshow("Horizontal",imgHor)
cv2.imshow("Vertical",imgVer)

cv2.imshow("Image Stack",imgStack)

cv2.waitKey(0)