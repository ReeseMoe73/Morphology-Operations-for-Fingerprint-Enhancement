import cv2

import numpy as np

img = cv2.imread('fingerprint.jpg')

(thresh, binary_img) = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

kernel = np.ones((5,5), np.uint8)

erosion = cv2.erode(binary_img, kernel, iterations = 1)

cv2.imshow('erosion', erosion)

cv2.waitKey(0)

cv2.destroyAllWindows()
