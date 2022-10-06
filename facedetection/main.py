import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)
cTime = 0
pTime = 0

mpFaceDetection = mp.solutions.face_detection
faceDetection = mpFaceDetection.FaceDetection()
mpDraw = mp.solutions.drawing_utils

stop=False
while stop==False:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = faceDetection.process(imgRGB)


    if results.detections:
        for id, detection in enumerate(results.detections):
            print(id,detection)
            print(detection.score)
            mpDraw.draw_detection(img,detection)
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, ic = img.shape
            bbox = int(bboxC.xmin * iw),int(bboxC.ymin * ih), \
                   int(bboxC.width * iw), int(bboxC.height * ih)
            cv2.rectangle(img,bbox, (255,0,255),2)
            cv2.putText(img,f'{int(detection.score[0] * 100)}%', (bbox[0],bbox[1]-20),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0,3))



    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    key = cv2.waitKey(15)

    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(0,255,0),3)
    cv2.imshow("Output",img)


    if key==ord('q'):
        stop=True