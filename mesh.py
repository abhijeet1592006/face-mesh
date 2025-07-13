#hi i am abhijeet singh and it is the base code. to detect 468 facial landmarks on face

import cv2

import mediapipe as mp

mpmesh=mp.solutions.face_mesh
draw=mp.solutions.drawing_utils

facemesh=mpmesh.FaceMesh()


cap=cv2.VideoCapture(0) 


while True:
    ok,frame=cap.read()

    rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    result=(facemesh.process(rgb))
    if (result.multi_face_landmarks):
        for i in result.multi_face_landmarks:
            for id,pos in enumerate(i.landmark):
                cx1=0
                cx2=0

                ih,iw,ic=frame.shape
                cx2=int(pos.x*iw)
                cy2=int(pos.y*ih)

                cv2.circle(frame,(cx2,cy2),2,(0,255,0),1)

                
           

            
    cv2.imshow("frame",frame)

    if(cv2.waitKey(1)==ord("q")):
        break

cv2.destroyAllWindows()
