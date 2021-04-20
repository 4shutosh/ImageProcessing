import numpy as np
import cv2

image1 = cv2.imread('F:\lena_color.jpg')
image2 = cv2.imread('F:\car.jpg')

image2 = cv2.resize(image2, (512, 512))

# addition
image1plus2 = cv2.add(image1, image2)
# image1plus2 = cv2.addWeighted(image1,0.5 image,0.5,0)
# we can also add two image with given weights to give a desired look to the result image a desired look
cv2.imshow("Addition + ", image1plus2)
cv2.waitKey(0)

# subtraction
imageSub = cv2.subtract(image1, image2)
cv2.imshow("Subtraction -", image1plus2)
cv2.waitKey(0)

# multiplication
image1plus2 = cv2.multiply(image1, image2)
cv2.imshow("Product *", image1plus2)
cv2.waitKey(0)

# divisiona
image1plus2 = cv2.divide(image1, image2)
cv2.imshow("Division /", image1plus2)
cv2.waitKey(0)

