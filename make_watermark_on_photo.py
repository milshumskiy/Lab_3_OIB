from PIL import Image
from main import save_edited_image
from main import add_to_edited_table

def watermark_photo(input_image_path, watermark_image_path, position):
    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path)

    # add watermark to image
    if (base_image.size > watermark.size):
        base_image.paste(watermark, position)
        save_edited_image(base_image, 'newimage.jpg')
        #base_image.show()
        #base_image.save(output_image_path)
        add_to_edited_table('newimage.jpg')
        print('The watermark was successfully applied to the picture')
    else:
        print('The size of the watermark is larger than the original photo !')
        return '123'



if __name__ == '__main__':
    watermark_photo('cat.jpg', 'ocean.jpg', position=(1, 1))