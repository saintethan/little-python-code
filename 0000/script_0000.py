'''
This script is based on Python3, which perfroms a funtion of adding a red number
on the top-right corner of a given image.
'''

import os.path
import random
import math
from PIL import Image, ImageDraw, ImageFont

# Get the absolute path of the image file
file_dir = os.path.abspath(os.path.dirname(__file__))
filename = "img.jpg"
file_path = os.path.join(file_dir, filename)
# print(file_path)

# Open an image file
image = Image.open(file_path)
# image.show()

# Set the font type, using true font
# Refer to the following system font folder on macOS
text_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc",
                               math.floor(min(image.size[:])/3))


# Generate a random number between 0~9
num = math.floor(10*random.random())

# Add a number on top-right corner of the original image
image_text = ImageDraw.Draw(image)
image_text.text((math.floor(image.size[0]*0.75),
                 math.floor(image.size[1])*0.06),
                str(num), font=text_font, fill=(255, 0, 0))

# Save the image with text on it
image.save(os.path.join(file_dir, 'img_text.jpg'))
