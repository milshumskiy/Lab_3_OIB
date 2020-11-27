from __future__ import print_function
import requests
import json
import cv2
import numpy as np

#imagename - isxodnoe izobrajenie
def save_image(image):
	filename='Processed image.png'
	cv2.imwrite(filename,image)

