import cv2

image1 = cv2.imread('F:\lena_color.jpg')
image2 = cv2.imread('F:\car.jpg')

# resizing for better output
image2 = cv2.resize(image2, (512, 512))

# AND
imageAnd = cv2.bitwise_and(image1, image2)
cv2.imshow("And ", imageAnd)
cv2.waitKey(0)

# OR
imageOr = cv2.bitwise_or(image1, image2)
cv2.imshow("OR ", imageOr)
cv2.waitKey(0)


# NOT
imageNot = cv2.bitwise_not(image1)
cv2.imshow("NOT ", imageNot)
cv2.waitKey(0)

# XOR
imageXor = cv2.bitwise_xor(image1, image2)
cv2.imshow("XOR ", imageXor)
cv2.waitKey(0)