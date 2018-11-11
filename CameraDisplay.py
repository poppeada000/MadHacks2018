#!/usr/bin/env python

import cv2
import numpy as np
import time
import Clarifmain

cap = cv2.VideoCapture(1)
def startCam():
        cap = cv2.VideoCapture(1)
        
        while True:
                ret, img = cap.read()
                cv2.imshow('lot',img)
                
                for i in range(1):
                        return_value, image = cap.read()
                        cv2.imwrite('opencv'+str(i)+'.jpg',image)
                if cv2.waitKey(2) & 0xFF == ord('p'):
                        Clarifmain.getSoda()

                if cv2.waitKey(0) & 0xFF == ord('q'):
                        return
                
                     
startCam()
cap.release()
cv2.destroyAllWindows()
