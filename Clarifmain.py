#!/usr/bin/env python

import os
import numpy as np
import cv2

from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

#APi Key for Clarifai
app = ClarifaiApp(api_key='cd72b128d29e43b39d9f932784380aa7')

def getSoda():
	model = app.models.get('MadHacks2018')
	image = ClImage(file_obj=open('opencv0.jpg', 'rb'))
	response=model.predict([image])
	concepts = response['outputs'][0]['data']['concepts']
	for concept in concepts:
    		print(concept['name'], concept['value'])

return

