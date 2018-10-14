from itertools import groupby

def look_and_say(string):
    res = ''
    for k, v in groupby(string):
        res += ''.join([str(len(list(v))), k])
    return res

element = '1'
end_result = 0

for i in range(30):
    element = look_and_say(element)
    end_result = len(element)

print(end_result)

# next problem: http://www.pythonchallenge.com/pc/return/5808.html 