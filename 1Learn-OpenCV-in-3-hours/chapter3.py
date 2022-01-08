import cv2
import numpy as np
# read image
img = cv2.imread("Resources/shapes.png")
# find size of image
print(img.shape)

# resize image. width=1000,height=500
imgResize = cv2.resize(img,(1000,500))
print(imgResize.shape)

# crop an image.[first height then width comes]
imgCropped = img[46:119,352:495]

cv2.imshow("Image",img)
#cv2.imshow("Image Resize",imgResize)

#display cropped image
cv2.imshow("Image Cropped",imgCropped)

cv2.waitKey(0)