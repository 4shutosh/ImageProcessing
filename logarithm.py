import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read an image
image = cv2.imread('F:\car.jpg')
image = cv2.resize(image, (512,512))

# Apply log transformation method
c = 255 / np.log(1 + np.max(image))
# C = scaling constant
# The value of ‘c’ is chosen such that we get the maximum  output value
# corresponding to the bit size used. So, the formula for calculating ‘c’ : c = 255 / (log (1 + max_input_pixel_value))
np.seterr(divide='ignore')
log_image = c * (np.log10(image + 1))
# formula for applying log transformation in an image is OUTPUT = c * log (1 + r)

# Specify the data type so that
# float value will be converted to int
log_image = np.array(log_image, dtype=np.uint8)

# Display both images
result = cv2.hconcat([image,log_image])
cv2.imshow("output", result)
cv2.waitKey(0)
