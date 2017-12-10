#! -*- coding: utf-8 -*-

import requests

# constants
RUN_URL = u'http://api.hackerearth.com/code/run/'

CLIENT_SECRET = '81b00a5cbbabde29b268730f9a7cefac8ca4174a'

source = open('test.py', 'r')
"""
test.py
#! -*- coding: utf-8 -*-

def square(no):
    return no * no

print(square(-23))
"""

data = {
    'client_secret': CLIENT_SECRET,
    'async': 0,
    'source': source.read(),
    'lang': "PYTHON",
    'time_limit': 5,
    'memory_limit': 262144,
}

r = requests.post(RUN_URL, data=data)
source.close()
print r.json()
