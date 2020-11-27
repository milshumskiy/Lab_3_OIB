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
