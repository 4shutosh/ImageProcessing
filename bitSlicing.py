import numpy as np
import cv2

imgInput = cv2.imread('F:\car.jpg', 0)
# reading image in grayscale (to work with 8 bits, colour image contains 16 bits)
img = cv2.resize(imgInput, (200, 200))
# resizing for better output

listBinary = []
# empty list
row, col = img.shape
# image.shape[0] is the number of row
# image.shape[1] is the number of column
for i in range(row):
    for j in range(col):
        listBinary.append(np.binary_repr(img[i][j], width=8))

# binary_repr  = returns the binary form the input number, where width is number of bits ex: 0000001

# We have a list of strings where each string represents binary pixel value
eight_bit_img = (np.array([int(i[0]) for i in listBinary], dtype=np.uint8) * 128).reshape(row, col)
seven_bit_img = (np.array([int(i[1]) for i in listBinary], dtype=np.uint8) * 64).reshape(row, col)
six_bit_img = (np.array([int(i[2]) for i in listBinary], dtype=np.uint8) * 32).reshape(row, col)
five_bit_img = (np.array([int(i[3]) for i in listBinary], dtype=np.uint8) * 16).reshape(row, col)
four_bit_img = (np.array([int(i[4]) for i in listBinary], dtype=np.uint8) * 8).reshape(row, col)
three_bit_img = (np.array([int(i[5]) for i in listBinary], dtype=np.uint8) * 4).reshape(row, col)
two_bit_img = (np.array([int(i[6]) for i in listBinary], dtype=np.uint8) * 2).reshape(row, col)
one_bit_img = (np.array([int(i[7]) for i in listBinary], dtype=np.uint8) * 1).reshape(row, col)
# np.unit8: implies a 8-bit integer representing from 0-255
# np.array: creates an array and the reshape function reshapes/makes it into the same matrix form using the same row and column
# so we obtain a same matrix of numbers (image) in each case
# as every number in listBinary is 8 in width (ex:00000000) so i[0] represents the MSB i.e the right most digit
# similarly the i[1], i[2] .. upto i[7] represents the each character
# this is called list comprehension in python, which results a new list of the same size of the list provided
# i.e a new list of the same size of listBinary, this list is now used to create a new array using the np.array and further
# reshape into the same matrix like the image, using the row and column
# Multiply with 2^(n-1) for the respective bit and the sliced bit image is formed, n = 1,2,3,4,5,6,7,8

# Add these images for ease of display in one image using cv2.hconcat() and cv2.vconcat()
final1 = cv2.hconcat([eight_bit_img, seven_bit_img, six_bit_img, five_bit_img])
final2 = cv2.hconcat([four_bit_img, three_bit_img, two_bit_img, one_bit_img])
final = cv2.vconcat([final1, final2])

cv2.imshow('bitSlicing Output', final)
cv2.waitKey(0)
