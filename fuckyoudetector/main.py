import mediapipe as mp
import cv2
import time


cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

cTime = 0
pTime = 0

stop = False
while stop == False:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLandmark in results.multi_hand_landmarks:
            for id, lm in enumerate(handLandmark.landmark):
                landmarkList = handLandmark.landmark
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                if id == 0:
                    cv2.circle(img,(cx,cy),9,(155,155,0),cv2.FILLED)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                indexTopY = int(landmarkList[8].y * h)
                indexDownY = int(landmarkList[6].y * h)
                ringTopY = int(landmarkList[16].y * h)
                ringDownY = int(landmarkList[14].y * h)
                pinkyTopY = int(landmarkList[20].y * h)
                pinkyDownY = int(landmarkList[18].y * h)
                # y2 = int(landmarkList[8].y * h)
                # y2 = int(landmarkList[8].y * h)
                middleFingerTopPointY = int(landmarkList[12].y * h)
                middleFingerDownPointY = int(landmarkList[10].y * h)
                print(middleFingerTopPointY, middleFingerDownPointY)
                if int(middleFingerTopPointY) < int(middleFingerDownPointY) and indexTopY > indexDownY and ringTopY > ringDownY and pinkyTopY > pinkyDownY:
                    cv2.putText(img,("FUCK YOU TOO, Idiot"),(70,100),cv2.FONT_HERSHEY_PLAIN,3,(255,255,0))
            # mpDraw.draw_landmarks(img,handLandmark,mpHands.HAND_CONNECTIONS)
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0))

    cv2.imshow("Output",img)
    key = cv2.waitKey(1)
    if key==ord('q'):
        stop=True
