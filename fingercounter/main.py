import mediapipe as mp
import cv2
import time


cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

cTime = 0
pTime = 0

fingerTipsIds = [4, 8, 12, 16, 20]

stop = False

while stop == False:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLandmark in results.multi_hand_landmarks:
            fingers = []
            landmarkList = handLandmark.landmark
            for id in range(0,5):
                if landmarkList[fingerTipsIds[id]].y < landmarkList[fingerTipsIds[id]-2].y:
                    fingers.append(1)
                else:
                    fingers.append(0)
            print(fingers)
            for id, lm in enumerate(handLandmark.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                # print(id,cx, cy)
                if id == 0:
                    cv2.circle(img,(cx,cy),9,(155,155,0),cv2.FILLED)
            mpDraw.draw_landmarks(img,handLandmark,mpHands.HAND_CONNECTIONS)
        # print(img.shape)
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0))

    cv2.imshow("Output",img)
    key = cv2.waitKey(1)
    if key==ord('q'):
        stop=True
