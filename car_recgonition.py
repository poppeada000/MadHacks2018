#!/usr/bin/env python

import cv2
import numpy as np
import time

def startCam():
	cap = cv2.VideoCapture(1)

	while True:
    		ret, img = cap.read()
    		cv2.imshow('lot',img)
    		for i in range(4):
        		return_value, image = cap.read()
        		cv2.imwrite('opencv'+str(i)+'.jpg',image)
    		if cv2.waitKey(1) & 0xFF == ord('q'):
        		break
	cap.release()
	cv2.destroyAllWindows()

return
