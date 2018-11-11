#!/usr/bin/env python

import numpy as np
import cv2
from matplotlib import pyplot as plt


def main():
    img = cv2.imread('opencv0.jpg')
    mask = np.zeros(img.shape[:2],np.uint8)

    bgdModel = np.zeros((1,65),np.float64)
    fgdModel = np.zeros((1,65),np.float64)

    rect = (200,150,900,950)

    cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
    mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
    img = img*mask2[:,:,np.newaxis]
    cv2.imwrite('opencvc.jpg',img)

main()
