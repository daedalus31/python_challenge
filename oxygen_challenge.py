import os
import re
import shutil

import requests
from PIL import Image

image_filename = 'oxygen.png'
response = requests.get('http://www.pythonchallenge.com/pc/def/oxygen.png', stream=True)
with open(image_filename, 'wb') as downloaded_image:
    shutil.copyfileobj(response.raw, downloaded_image)
del response

image = Image.open(image_filename)
pixels = image.load()

middle_row = [pixels[x, image.size[1] / 2] for x in range(image.size[0])]
result = ''.join([chr(middle_row[i][0]) for i in range(4, len(middle_row), 7)])


print(''.join([chr(int(i)) for i in re.findall(r'\d+', result)]))

os.remove(image_filename)
