import cv2
import mediapipe as mp
import time
import HandTrackingModule as hm
import numpy as np
import pandas as pd
import pickle
import math

pTime = 0
cTime = 0
largura_janela = 640
altura_janela = 480
cap = cv2.VideoCapture(1)
cap.set(3, largura_janela)
cap.set(4, altura_janela)

detector = hm.handDetector(static_image_mode=False, max_num_hands=1)
labels_dict = {0: 'A', 1: 'B', 2: 'L'}
# count = 1
while True:
    success, img = cap.read()
    lm_list, img = detector.findHands(img, draw=True, getPosition=True)
    if lm_list:
        lm_lenght, img = detector.appendDistance(lm_list, img)
        # print(lm_lenght)
    
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime 
    
    cv2.putText(img, f'FPS: {str(int(fps))}', (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)
    cv2.imshow("Image", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows() 