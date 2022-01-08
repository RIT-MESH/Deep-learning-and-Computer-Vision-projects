import cv2
import numpy as np
# type of object uint8 = unsigned integer with 8 bit i.e from 0-255
img = np.zeros((512,512,3),np.uint8)
#print(img)
#img[:]= 255,0,0

# draw a line
# cv2.line(image, (starting point of image),(ending point of image),(define color),define thickness)
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)

# cv2.rectangle(image, (starting point of image),(ending point of image),(define color),define thickness)
cv2.rectangle(img,(0,0),(250,350),(0,0,255),2)

# cv2.circle(image, (center point of circle),radius of circle,(define color),define thickness)
cv2.circle(img,(400,50),30,(255,255,0),5)

# put text in image
cv2.putText(img," OPENCV  ",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),3)


cv2.imshow("Image",img)

cv2.waitKey(0)