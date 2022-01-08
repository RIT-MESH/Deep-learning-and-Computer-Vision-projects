import cv2
import numpy as np

# read image
img = cv2.imread("Resources/cards.jpg")

width,height = 250,350

# define 4 corner point of card
# To get these points open in paints and as you move the cursor
# the points will show in the bottom.
pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)

# Get output image based on Perspective
imgOutput = cv2.warpPerspective(img,matrix,(width,height))


cv2.imshow("Image",img)
cv2.imshow("Output",imgOutput)

cv2.waitKey(0)