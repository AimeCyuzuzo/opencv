import cv2
import numpy as np

# img = cv2.imread("basics/try.jpg")
# cv2.imshow("Output",img)
# cv2.waitKey(0)

#### CODE FROM ANOTHER VIDEO BUT NOT WORKING -- CAN'T FIND CAMERA DEVICE

# webcam = cv2.VideoCapture(-1)


# stop=False
# while stop==False:
#     ret,frame = webcam.read()

#     if ret==True:
#         cv2.imshow("Aime",frame)
#         key=cv2.waitKey(1)
#         if key==ord('q'):
#             stop=True


#### END OF CODE FROM ANOTHER VIDEO BUT NOT WORKING -- CAN'T FIND CAMERA DEVICE



### WEBCAM SAMPLE FROM THE ACTUAL VIDEO



# cap = cv2.VideoCapture(-1)
# cap.set(3,640)
# cap.set(4,480)

# while True:
#     success, img = cap.read()
#     cv2.imshow("Video", img)
#     if cv2.waitKey(1) & 0xFF ==ord('q'):
#         break

 
### END WEBCAM SAMPLE FROM THE ACTUAL VIDEO

kernel = np.ones((2,2),np.uint8)
kernel1 = np.ones((1,1),np.uint8)

img = cv2.imread("basics/try.jpg")
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(img,(9,9),0)
imgCanny = cv2.Canny(img,100,100)
imgDilation = cv2.dilate(imgCanny,kernel=kernel,iterations=1)
imgEroded = cv2.erode(imgDilation,kernel=kernel1,iterations=1)

cv2.imshow("Output",img)
cv2.imshow("Output",imgBlur)
cv2.imshow("Output",imgCanny)
cv2.imshow("Output",imgDilation)
cv2.imshow("Output",imgEroded)

cv2.waitKey(0)
#22:26
