import  cv2
import  mediapipe as mp
import  time

cap = cv2.VideoCapture("videos/1_inana.mp4")
cap = cv2.VideoCapture(0)

mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils

cTime = 0
pTime = 0

stop = False
while stop==False:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    print(results.pose_landmarks)

    if results.pose_landmarks:
        mpDraw.draw_landmarks(img,results.pose_landmarks,mpPose.POSE_CONNECTIONS)



    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,255,0),5)

    cv2.imshow("Output",img)
    key = cv2.waitKey(1)
    if key==ord('q'):
        stop=True
