import cv2
import numpy as np

image = cv2.imread('F:\car.jpg', 0)
image = cv2.resize(image, (512, 512))


# imageSquareRoot = cv2.sqrt(image, image)
imageSquareRoot = np.sqrt(image)

cv2.imshow("Square Root", imageSquareRoot)
cv2.waitKey(0)