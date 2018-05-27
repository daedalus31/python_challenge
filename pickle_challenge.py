import urllib.request
import pickle

url = 'http://www.pythonchallenge.com/pc/def/banner.p'
resp = urllib.request.urlopen(url)
unpickled = pickle.loads(resp.read())
for it in unpickled:
    for item in it:
        print(''.join([item[0]] * item[1]), end='')
    print()

