#!/usr/bin/env python

import cv2
import numpy as np
import matplotlib.pyplot as plt
import time

cap = cv2.VideoCapture(1)

bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)


while True:

    ret, img = cap.read()


    #cv2.rectangle(img,(200,150),(900,950),(0,0,255),5)
    cv2.imshow('lot',img)

    for i in range(4):
        return_value, image = cap.read()
        cv2.imwrite('opencv'+str(i)+'.jpg',image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



cap.release()
cv2.destroyAllWindows()
