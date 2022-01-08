######################## READ IMAGE ############################
# import cv2
# # LOAD AN IMAGE USING 'IMREAD'
# img = cv2.imread("Resources/lena.png")
# # DISPLAY
# cv2.imshow("Lena Soderberg",img)
# cv2.waitKey(0)

######################### READ VIDEO #############################
# import cv2
# frameWidth = 640
# frameHeight = 480
# cap = cv2.VideoCapture("Resources/test_ video.mp4")
# while True:
#     success, img = cap.read()
#     img = cv2.resize(img, (frameWidth, frameHeight))
#     cv2.imshow("Result", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
######################### READ WEBCAM  ############################
import cv2
frameWidth = 640
frameHeight = 480
# select webcam
# 0 will select default webcamera
cap = cv2.VideoCapture(0)

# set frame size
cap.set(3, frameWidth)
cap.set(4, frameHeight)

#change brightness. Id for it is 10
cap.set(10,150)
while True:
    success, img = cap.read()
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
