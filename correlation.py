import cv2
import numpy as np

# read image
src = cv2.imread('F:\car.jpg', 0)
src = cv2.resize(src, (512, 512))

# prepare the filter
kernel = [[2, 2, 2], [1, 1, 1], [1, 3, 2]]
# took random elements for kernel

# apply kernel to the original image
dst = cv2.filter2D(src, -1, np.array(kernel))
# Correlation Filtering

# concatenate images horizontally
result = np.concatenate((src, dst), axis=1)
# cv2.imwrite('result.png', result)
cv2.imshow("output", result)
cv2.waitKey(0)