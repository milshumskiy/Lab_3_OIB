import os
import cv2
from datetime import datetime
from PIL import Image
from sqlalchemy import *
from sqlalchemy.orm import *


def save_original_image(image, file_name):
    # try:
    if os.path.exists('Original') == 0:
        os.mkdir('Original')
        os.chmod(r'Original', 0o777)
    directory = os.path.abspath(os.curdir) + '\\Original\\'
    list_of_files = os.listdir(directory)
    copy_counter = 0
    i = 0
    index = file_name.find('.')
    if len(list_of_files) != 0:
        while True:
            if list_of_files[i] == file_name or list_of_files[i] == file_name[:index] + str(
                    copy_counter) + file_name[index:]:
                copy_counter = copy_counter + 1
            i = i + 1
            if i >= len(list_of_files):
                break

    if copy_counter > 0:
        file_name = file_name[:index] + str(copy_counter) + file_name[index:]

    path = directory + file_name
    cv2.imwrite(path, image)


# except Exception as e:
# print("Oops!", e.__class__, "occurred.")


def save_edited_image(base_image, output_image_name):
    try:
        if os.path.exists('Edited') == 0:
            os.mkdir('Edited')
            os.chmod(r'Edited', 0o777)
        directory = os.path.abspath(os.curdir) + '\\Edited\\'
        list_of_files = os.listdir(directory)
        copy_counter = 0
        i = 0
        index = output_image_name.find('.')
        if len(list_of_files) != 0:
            while True:
                if list_of_files[i] == output_image_name or list_of_files[i] == output_image_name[:index] + str(
                        copy_counter) + output_image_name[index:]:
                    copy_counter = copy_counter + 1
                i = i + 1
                if i >= len(list_of_files):
                    break

        if copy_counter > 0:
            output_image_name = output_image_name[:index] + str(copy_counter) + output_image_name[index:]

        path = directory + output_image_name

        base_image.save(path)
    except Exception as e:
        print("Oops!", e.__class__, "occurred.")

