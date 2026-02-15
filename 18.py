import cv2

import numpy as np

image=  cv2.imread("download (1).jpeg")

sharpen_kernel = np.array([
    [0,-1,0],
    [-1,5,-1],
    [0,-1,0]
])


sharpened = cv2.filter2D(image, -1 , sharpen_kernel)


cv2.imshow("Original Image",image)
cv2.imshow("Sharp Image",sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()