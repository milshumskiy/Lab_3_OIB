from __future__ import print_function
import requests
import json
import cv2
import numpy as np

#imagename - isxodnoe izobrajenie
def save_image(image):
	filename='Processed image.png'
	cv2.imwrite(filename,image)

def get_watermark_image(imagename):
	try:	
		addr = 'http://localhost:5000'
		test_url = addr + '/api/test'
		content_type = 'image/jpeg'
		headers = {'content-type': content_type}
		img = cv2.imread(imagename)
		_, img_encoded = cv2.imencode('.jpg', img)
	

		