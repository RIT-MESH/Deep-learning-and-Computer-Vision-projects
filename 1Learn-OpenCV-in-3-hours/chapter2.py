import cv2
import numpy as np
# read image
img = cv2.imread("Resources/lena.png")
# np.ones= all values are 1. size of matrix is 5x5. then type
# of object uint8 = unsigned integer with 8 bit i.e from 0-255
kernel = np.ones((5,5),np.uint8)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# blur image
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
# canny edge detector
imgCanny = cv2.Canny(img,150,200)
# increase the thickness of edges
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
# opposite of dialation is erosion
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)

cv2.imshow("Gray Image",imgGray)
cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Dialation Image",imgDialation)
cv2.imshow("Eroded Image",imgEroded)
cv2.waitKey(0)