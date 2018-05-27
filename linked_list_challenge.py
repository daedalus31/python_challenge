import re

import requests

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
nothing = 12345

while True:
    resp = requests.get(url, params={'nothing': nothing}).text
    print(resp)
    try:
        nothing = re.findall('and the next nothing is [0-9]+', resp)[0]
        nothing = int(nothing.lstrip('and the next nothing is '))
    except IndexError:
        if 'Divide by two' in resp:
            nothing = nothing/2
        elif '.html' in resp:
            break
