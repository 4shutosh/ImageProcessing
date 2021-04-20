import cv2
import numpy as np

img = cv2.imread('F:\car.jpg', 0)
img  = cv2.resize(img,(512,512))

# kernel
kernel = np.ones((5,5),np.uint8)
#erosion
erosion = cv2.erode(img,kernel,iterations = 1)

# dilation
dilation = cv2.dilate(img,kernel,iterations = 1)

cv2.imshow("errossion", erosion)
cv2.waitKey(0)


cv2.imshow("dilation", dilation)
cv2.waitKey(0)