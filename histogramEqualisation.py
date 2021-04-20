import cv2
import numpy as np

from matplotlib import pyplot as plt


imgInput = cv2.resize(imgInput, (500, 500))
# taking image input as a grayscale image, 0 represents grayscale

hist, bins = np.histogram(imgInput.flatten(), 256, [0, 256])
# np.histogram returns an array which is stored in hist, which requires a linear array which is obtained using the
# numpy.ndarrray.flatten()

cdf = hist.cumsum()
# Returns the cumulative sum of the elements along a given axis (cdf)
cdf_normalized = cdf*hist.max()/cdf.max()

# this plot is for normal un processed image histogram with its respective cdf graph
plt.plot(cdf_normalized, color='b')  # plotting cdf
plt.hist(imgInput.flatten(), 256, [0, 256], color='r')  # ploting histogram
plt.xlim([0, 256]) # setting limit to x axis
plt.legend(('cdf', 'histogram'), loc='upper left')
plt.show()

cdf_m = np.ma.masked_equal(cdf, 0)
# we used masked array to exclude all the 0 values in cdf (masked 0)
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
# applied the equation obtained from wikipedia for histogram equalization
cdf = np.ma.filled(cdf_m, 0).astype('uint8')
# the masked values are filled again with the valued provided other than the array i.e 0 here. the type is defined are uint8 for the image formation again

img2 = cdf[imgInput]

hist2, bins2 = np.histogram(img2.flatten(), 256, [0, 256])
# histogram returns an array

cdf2 = hist2.cumsum()
cdf_normalized2 = cdf2*hist2.max()/cdf2.max()

# this plot is for histogram equalized image histogram with its respective cdf graph
plt.plot(cdf_normalized2, color='b')
plt.hist(img2.flatten(), 256, [0, 256], color='r')
plt.xlim([0, 256])
plt.legend(('cdf', 'histogram'), loc='upper left')
plt.show()

final = cv2.hconcat([imgInput, img2])
# side by side output of images before and after histogram equalization
cv2.imshow('output of images', final)
cv2.waitKey(0)



