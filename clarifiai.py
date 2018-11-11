import numpy as np
import cv2
from matplotlib import pyplot as plt
from clarifai.rest import ClarifaiApp

img = cv2.imread('opencv0.jpg')

clarifai_api = ClarifaiApi()
result = Clarifai_api.tag_images(open('image.jpg'))
