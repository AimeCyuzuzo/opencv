import mediapipe as mp
import cv2
import time

cap = cv2.VideoCapture('videos/1_inana.mp4')
cTime = 0
pTime = 0

mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=5)
mpDraw = mp.solutions.drawing_utils

stop = False
while stop==False:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = faceMesh.process(imgRGB)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.imshow("Output",img)
    key = cv2.waitKey(1)
    if key==ord('q'):
        stop=True
