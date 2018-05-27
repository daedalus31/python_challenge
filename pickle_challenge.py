import pickle

import requests

url = 'http://www.pythonchallenge.com/pc/def/banner.p'
resp = requests.get(url)
for it in pickle.loads(resp.content):
    for item in it:
        print(''.join([item[0]] * item[1]), end='')
    print()
