import mediapipe as mp
import cv2
import time
import numpy as np
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_,CLSCTX_ALL, None
)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volume.GetMute()
volume.GetMasterVolumeLevel()
volumeRange = volume.GetVolumeRange()
minimumVolume = volumeRange[0]
maximumVolume = volumeRange[1]


cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils

cTime = 0
pTime = 0

stop = False
while stop == False:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLandmark in results.multi_hand_landmarks:
            for id, lm in enumerate(handLandmark.landmark):
                landmarkList = handLandmark.landmark
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                x1 = int(landmarkList[4].x*w)
                y1 = int(landmarkList[4].y*h)
                x2 = int(landmarkList[8].x*w)
                y2 = int(landmarkList[8].y*h)
                xMiddle = int((x1+x2)/2)
                yMiddle = int((y1+y2)/2)
                print(xMiddle)
                print(yMiddle)
                if id == 8:
                    cv2.circle(img, (cx, cy), 9, (100, 100, 100), cv2.FILLED)
                if id == 4:
                    cv2.circle(img, (cx, cy), 9, (100, 100, 100), cv2.FILLED)
                # print(x1,y1,x2,y2)
                cv2.line(img,(x1,y1),(x2,y2),(155,155,0),3)

                length = math.hypot(x2-x1,y2-y1)
                print(length)
                convertedVirtualVolume = np.interp(length,[25,130],[minimumVolume,maximumVolume])
                print(convertedVirtualVolume)
                volume.SetMasterVolumeLevel(convertedVirtualVolume,None)


                volumeToDisplay = np.interp(length,[25,130],[350,70])
                currentVolume = np.interp(length,(25,130),[0,100])
                cv2.putText(img,f'{str(int(currentVolume))}%',(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0))

                cv2.rectangle(img,(50,70),(85,350),(0,0,0),2)
                cv2.rectangle(img, (50, int(volumeToDisplay)), (85, 350), (60, 0, 0), cv2.FILLED)

                cv2.circle(img,(xMiddle,yMiddle),9,(255,0,0),cv2.FILLED)
                if length < 25:
                    cv2.circle(img,(xMiddle,yMiddle),9,(0,0,255),cv2.FILLED)
                if length > 130:
                    cv2.circle(img,(xMiddle,yMiddle),9,(0,255,0),cv2.FILLED)

            # mpDraw.draw_landmarks(img,handLandmark,mpHands.HAND_CONNECTIONS)
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    # cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0))

    cv2.imshow("Output",img)
    key = cv2.waitKey(1)
    if key==ord('q'):
        stop=True
