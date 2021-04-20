import cv2
import numpy as np
from scipy import ndimage
# read image
src = cv2.imread('F:\car.jpg', 0)
src = cv2.resize(src, (512, 512))

# prepare the filter
kernel = np.array([[1, 1, 1], [1, 1, 0], [1, 2, 2]])
# apply kernel to the original image using convolution filtering
dst_conv = ndimage.convolve(src, kernel, mode='constant', cval=1.0)

# concatenate images horizontally
result = np.concatenate((src, dst_conv), axis=1)
cv2.imshow("output", result)
cv2.waitKey(0)