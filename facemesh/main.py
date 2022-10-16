import mediapipe as mp
import cv2
import time

cap = cv2.VideoCapture(0)
pTime = 0

mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=5)

mpDraw = mp.solutions.drawing_utils
drawSpec = mpDraw.DrawingSpec(thickness=1,circle_radius=2)

stop = False
while stop==False:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = faceMesh.process(imgRGB)
    if results.multi_face_landmarks:
        for faceLandmarks in results.multi_face_landmarks:
            mpDraw.draw_landmarks(img,faceLandmarks,mpFaceMesh.FACEMESH_CONTOURS,drawSpec,drawSpec)
            for id, lm in enumerate(faceLandmarks.landmark):
                iw, ih, ic = img.shape
                cx, cy = int(lm.x*iw), int(lm.y*ih)
                print(id, cx, cy)


    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.imshow("Output",img)
    key = cv2.waitKey(20)
    if key==ord('q'):
        stop=True
