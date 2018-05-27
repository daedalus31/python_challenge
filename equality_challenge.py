import re

import requests

url = 'http://www.pythonchallenge.com/pc/def/equality.html'

mess = re.findall('<!--(.*?)-->', str(requests.get(url).content))[0]

letters = re.findall('[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]', mess)
print(''.join([l[4] for l in letters]))
