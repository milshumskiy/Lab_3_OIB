from flask import Flask, request, Response,make_response
import jsonpickle
import numpy as np
from PIL import Image
import numpy
import cv2
import io
import StringIO
from prog import watermark_photo
from save_instruments import save_original_image, save_edited_image, add_to_origin_table, add_to_edited_table
import os


# Initialize the Flask application
app = Flask(__name__)
app.debug = True


@app.route('/api/test', methods=['POST'])
def test():
    r = request
    
   
    # convert string of image data to uint8
    nparr = np.fromstring(r.data, np.uint8)
    # decode image
    filename='prinytoe.jpg'
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    save_original_image(img,filename)
    add_to_origin_table(filename)
    path_to_original = os.path.abspath(os.curdir) + '\\Original\\'+ filename
    recieved_counter = 0
    edited_name = 'edited' + str(recieved_counter) + '.jpg'
    path_to_edited = os.path.abspath(os.curdir) + '\\Edited\\'+ edited_name

    watermark_photo(path_to_original, edited_name, '2.jpg', position=(1, 1))
    recieved_counter = recieved_counter + 1
   
