import numpy as np
import cv2
from matplotlib import pyplot as plt
imgInput = cv2.imread('F:\car.jpg')
from PIL import Image, ImageFilter

# reading image in grayscale (to work with 8 bits, colour image contains 16 bits)
image = cv2.resize(imgInput, (512, 512))

image2 = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)
image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
figure_size = 9
new_image = cv2.blur(image2,(figure_size, figure_size))
plt.figure(figsize=(11,6))
plt.subplot(121), plt.imshow(image2, cmap='gray'),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(new_image, cmap='gray'),plt.title('Mean filter')
plt.xticks([]), plt.yticks([])
plt.show()