import cv2

image = cv2.imread('F:\car.jpg')
image = cv2.resize(image, (512, 512))

# square
imageSquare = cv2.multiply(image, image)
cv2.imshow("Square of image ", imageSquare)
cv2.waitKey(0)