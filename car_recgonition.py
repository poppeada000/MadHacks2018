import cv2
from clarifai.rest import ClarifaiApp
import numpy as np
import matplotlib.pyplot as plt
import time
import image_brake

#tenserflow
#mlkit 
cap = cv2.VideoCapture(1)

bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('output', fourcc, 20.0, (640,480))

while True:
    ret, img = cap.read()
    #gray = cv2.cvtColor()
    cv2.rectangle(img,(200,150),(400,350),(0,0,255),5)
    cv2.imshow('lot',img)
    for i in range(4):
        return_value, image = cap.read()
        cv2.imwrite('opencv'+str(i)+'.jpg',image)

        #time.sleep(.2)
    #cv2.grabCut(img,mask,rect,bgdModel,fgdModel5,cv2.GC_INIT_WITH_RECT)
    #mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
    #img = img*mask2[:,:,np.newaxis]
    if cv2.waitKey(1) & 0xFF == ord('q'):
       break


cap.release()
#out.release()
cv2.destroyAllWindows()
