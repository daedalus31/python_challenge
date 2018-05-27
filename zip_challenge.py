import re
from zipfile import ZipFile

nothing = 90052
comments = []

with ZipFile('channel.zip') as archive:
    while True:
        comments.append(archive.getinfo(str(nothing) + '.txt').comment.decode('utf-8'))
        with archive.open(str(nothing) + '.txt') as file:
            file_content = file.read().decode('utf-8')
            try:
                nothing = re.findall('ext nothing is [0-9]+', file_content)[0]
                nothing = int(nothing.lstrip('ext nothing is '))
            except IndexError:
                print(file_content)
                break

print(''.join(comments))
