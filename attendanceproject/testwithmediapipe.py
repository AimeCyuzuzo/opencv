import  cv2
import  mediapipe as mp
import  time
import face_recognition as fr
import os
from datetime import datetime
import numpy as np

cap = cv2.VideoCapture("videos/1_inana.mp4")
cap = cv2.VideoCapture(0)

mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils

cTime = 0
pTime = 0




path = "attendanceproject/images"
images = []
classNames = []
myList = os.listdir(path)
print(myList)

for classs in myList:
    currentImage = cv2.imread(f'{path}/{classs}')
    images.append(currentImage)
    classNames.append(os.path.splitext(classs)[0])

print(classNames)

def findEncodings(images):
    encodeList = []
    for image in images:
        image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        encodeImage = fr.face_encodings(image)[0]
        encodeList.append(encodeImage)
    return encodeList               


def markAttendance(name):
    with open('attendanceproject/attendancesheet.csv', 'r+') as f:
        myDataList = f.readlines()
        # print(myDataList)
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            #TO GET THE TIME ONLY IN A STRING FORMAT(If you know the day, just need the time)   dateTimeString = now.strftime('%H:/%M:/S') 
            f.writelines(f'\n{name},{now}')
            




encodeListKnown = findEncodings(images)
print(len(encodeListKnown))
print("Encoding Complete.")

cap = cv2.VideoCapture(0)




stop = False
while stop==False:
    success, img = cap.read()
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = pose.process(img)
    print(results.pose_landmarks)

    if results.pose_landmarks:
        mpDraw.draw_landmarks(img,results.pose_landmarks,mpPose.POSE_CONNECTIONS)






    facesLocation = fr.face_locations(img)
    facesEncoded = fr.face_encodings(img,facesLocation)
    for faceEncoded, faceLocation in zip(facesEncoded,facesLocation):
        matches = fr.compare_faces(encodeListKnown,faceEncoded)
        # print(matches)
        facesDistances = fr.face_distance(encodeListKnown,faceEncoded)
        # print(facesDistances)

        matchIndex = np.argmin(facesDistances)
        print(matchIndex)

        y1, x2, y2, x1 = faceLocation
        cv2.rectangle(img,(x1,y1),(x2,y2),(255,120,0),3)

        if matches[matchIndex]:
            if facesDistances[matchIndex]<0.5:
                matchIndexy1, x2, y2, matchIndexx1 = faceLocation
                cv2.rectangle(img,(x1,y1),(x2,y2),(120,255,0),3)
                name = classNames[matchIndex]

                markAttendance(name)
                # cv2.rectangle(img,(x1,y1-35),(x2,y1+5),(120,255,0),cv2.FILLED)
                cv2.putText(img,f'{classNames[matchIndex]}',(int(matchIndexx1)-5,int(matchIndexy1)),cv2.FONT_ITALIC,1,(255,120,0),2)
            



        



    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,255,0),5)

    cv2.imshow("Output",img)
    key = cv2.waitKey(1)
    if key==ord('q'):
        stop=True
