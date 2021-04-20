import cv2
import numpy as np

image = cv2.imread('F:\car.jpg').astype(np.float32) / 255
# Load an image and convert it to one with floating-point elements in range [0,1]

image = cv2.resize(image, (512, 512))

# varianceImage = np.var(image2)
# print(varianceImage)

image -= image.mean()
image /= image.std()
# To normalize a matrix—that is, to get a zero-mean
# and unit-variance matrix—we need to subtract the mean value,
# which we can get by calling mean and dividing the matrix by its standard deviation.
# we can also use cv2.meanStdDev which computes both mean and standard deviation simultaneously


cv2.imshow("Example", image)
cv2.waitKey(0)

