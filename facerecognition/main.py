import cv2
import numpy as np
import face_recognition as fr

imgAime = fr.load_image_file("facerecognition/images/2.png")
imgAimeRGB = cv2.cvtColor(imgAime,cv2.COLOR_BGR2RGB)
imgAime2 = fr.load_image_file("facerecognition/images/3.png")
imgAime2RGB = cv2.cvtColor(imgAime2,cv2.COLOR_BGR2RGB)
imgTest = fr.load_image_file("facerecognition/images/1.png")
imgTestRGB = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)

faceLocation = fr.face_locations(imgAime)[0]
encodedImage = fr.face_encodings(imgAime)[0]
cv2.rectangle(imgAime,(faceLocation[3],faceLocation[0]),(faceLocation[1],faceLocation[2]),(255,0,0),3)
print(faceLocation)
print(faceLocation)
print(faceLocation)
print(faceLocation)
print(faceLocation)
print(faceLocation)

faceLocation2 = fr.face_locations(imgAime2)[0]
encodedImage2 = fr.face_encodings(imgAime2)[0]
cv2.rectangle(imgAime2,(faceLocation[3],faceLocation[0]),(faceLocation[1],faceLocation[2]),(255,0,0),3)


faceLocationImgTest = fr.face_locations(imgTest)[0]
encodedImgTest = fr.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(faceLocation[3],faceLocation[0]),(faceLocation[1],faceLocation[2]),(255,0,0),3)



results = fr.compare_faces([encodedImage],encodedImgTest)
print(results)
faceDistance = fr.face_distance([encodedImage],encodedImgTest)
print(faceDistance)
cv2.putText(imgTest,f'{results} {round(faceDistance[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255),3)


stop = False
while stop==False:
    cv2.imshow("Aime Cyuzuzo", imgAime)
    # cv2.imshow("Aime Cyuzuzo",imgAime2)
    cv2.imshow("Aime Cyuzuzo - Test", imgTest)
    key = cv2.waitKey(1)
    if key == ord("q"):
        stop = True