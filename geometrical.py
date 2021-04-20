import cv2
import numpy as np


# image1 = cv2.imread('F:\lena_color.jpg')
image2 = cv2.imread('F:\car.jpg')

# resize : scaling of image
imageResized = cv2.resize(image2, (512, 512))
cv2.imshow("resized", imageResized)
cv2.waitKey(0)

# rotation of image
rows, col, ch = image2.shape
matrix = cv2.getRotationMatrix2D((col/2, rows/2), 90, 1)
dst = cv2.warpAffine(image2, matrix, (col, rows))
dst1= cv2.resize(dst,(512,512))
cv2.imshow("rotated", dst1)
cv2.waitKey(0)

# perspective transformation
pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])

matrix2 = cv2.getPerspectiveTransform(pts1, pts2)
result = cv2.warpPerspective(image2, matrix2, (300, 300))
cv2.imshow("changed perspective", result)
cv2.waitKey(0)



