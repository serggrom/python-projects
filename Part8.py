
poem = '''There was a young lady named Bright,
Whose speed was far faster then light:
She started one day
In a relative way,
And returned on the previous night.'''

'''
print(len(poem))

fout = open('relativity', 'wt')
'''

#fout.write(poem)
#print(poem, file=fout)
#print(poem, file=fout, sep='', end='')
#fout.close()
'''
size = len(poem)
offset = 0
chunk = 100
while True:
    if offset > size:
        break
    fout.write(poem[offset:offset+chunk])
    offset +=chunk

fout.close()
'''

#fout = open('relativity', 'xt')
'''
try:
    fout = open('relativity', 'xt')
    fout.write('stomp stomp stomp')
except FileExistsError:
    print('relativity already exists! That was a close one.')
'''

'''
fin = open('relativity', 'rt')
poem = fin.read()
fin.close()
print(len(poem))
'''


'''
poem2 = ''
fin = open('relativity', 'rt')
chunk = 100
while True:
    fragment = fin.read(chunk)
    if not fragment:
        break
    poem2 += fragment

fin.close()
print(len(poem2))
'''

'''
poem2 = ''
fin = open('relativity', 'rt')
while True:
    line = fin.readline()
    if not line:
        break
    poem2 += line

fin.close()
print(len(poem2))
'''

'''
poem2 = ''
fin = open('relativity', 'rt')
for line in fin:
    poem2 += line

fin.close()
print(len(poem2))
print(poem2)
'''

'''
fin = open('relativity', 'rt')
lines = fin.readlines()
fin.close()
print(len(lines), 'lines read')
for line in lines:
    print(line, end='')
'''

'''
bdata = bytes(range(0, 256))
print(len(bdata))

fout = open('bfile', 'wb')
fout.write(bdata)
fout.close()

fout = open('bfile', 'wb')
size = len(bdata)
offset = 0
chunk = 100
while True:
    if offset > size:
        break
    fout.write(bdata[offset:offset+chunk])
    offset += chunk
fout.close()


fin = open('bfile', 'rb')
bdata = fin.read()
print(len(bdata))
fin.close()

with open('bfile', 'wb') as fout:
    fout.write(bdata)



fin = open('bfile', 'rb')
print(fin.tell())
fin.seek(255)
print(fin.seek(255))

bdata = fin.read()
print(len(bdata))
print(bdata[0])




import os

print(os.SEEK_SET)
print(os.SEEK_CUR)
print(os.SEEK_END)


fin = open('bfile', 'rb')
print(fin.seek(-1, 2))
print(fin.tell())

bdata = fin.read()
print(len(bdata))
print(bdata[0])

fin = open('bfile', 'rb')
print(fin.seek(254, 0))
print(fin.tell())

print(fin.seek(1, 1))
print(255)

bdata = fin.read()

print(len(bdata))
print(bdata[0])
'''

'''
import csv
villains = [
    ['Doctor', 'No'],
    ['Rosa', 'Klebb'],
    ['Mister', 'Big'],
    ['Auric', 'Goldfinger'],
    ['Ernst', 'Blofeld']
]
with open('villains', 'wt') as fout:
    csvout = csv.writer(fout)
    csvout.writerows(villains)


with open('villains', 'rt') as fin:
    cin = csv.reader(fin)
    villains = [row for row in cin]
print(villains)


with open('villains', 'rt') as fin:
    cin = csv.DictReader(fin, fieldnames=['first', 'last'])
    villains = [row for row in cin]

print(villains)

villains = [
    {'last': 'No', 'first': 'Doctor'},
    {'last': 'Klebb', 'first': 'Rosa'},
    {'last': 'Big', 'first': 'Mister'},
    {'last': 'Goldfinger', 'first': 'Auric'},
    {'last': 'Blofeld', 'first': 'Ernst'}]
with open('villains', 'wt') as fout:
    cout = csv.DictWriter(fout, ['first', 'last'])
    cout.writeheader()
    cout.writerows(villains)
print(villains)
'''



'''
import xml.etree.ElementTree as et
tree = et.ElementTree(file='menu.xml')
root = tree.getroot()
assert isinstance(root, object)
root.tag

for child in root:
    print('tag:', child, 'attributes:', child.attrib)
for grandchild in root:
    print('\ttag:', grandchild.tag, 'attributes:', grandchild.attrib)
tag: breakfast attributes: {'hours': '7-11'}
    tag: item attributes: {'price': '$6.00'}

print(len(root))
'''

'''
menu = \
{
 "breakfast": {
    "hours": "7-11",
    "items": {
            "breakfast burritos": "$6.00",
            "pancakes": "$4.00"
            }
        },
"lunch" : {
            "hours": "11-3",
            "items": {
                    "hamburger": "$5.00"
                    }
        },
"dinner": {
            "hours": "3-10",
            "items": {
                    "spaghetti": "$8.00"
                    }
            }
}

import json
menu_json = json.dumps(menu)
print(menu_json)

menu2 = json.loads(menu_json)
print(menu2)


import datetime
now = datetime.datetime.utcnow()
print(now)
#print(json.dumps(now))

now_str = str(now)
print(json.dumps(now_str))

from time import  mktime
now_epoch = int(mktime(now.timetuple()))
print(json.dumps(now_epoch))


class DTEncoder(json.JSONEncoder):
    def default(self, obj):
        #isinstance() check the type of obj
        if isinstance(obj, datetime.datetime):
            return int(mktime(obj.timetuple()))
        # else it's something the normal decoder knows:
        return json.JSONEncoder.default(self, obj)


json.dumps(now, cls=DTEncoder)
print(json.dumps(now, cls=DTEncoder))

print(type(now))
print(isinstance(now, datetime.datetime))
print(type(234))
print(type('hey'))
print(isinstance('hey', str))
'''

'''
import yaml
with open('mcintyre.yaml', 'rt') as fin:
    text = fin.read()
data = yaml.load(text)
print(data['details'])
'''


'''
import configparser
cfg = configparser.ConfigParser()
cfg.read('settings.cfg')
print(cfg)
cfg['french']
cfg['french']['greeting']
'''


'''
import pickle
import datetime
now1 = datetime.datetime.utcnow()
pickled = pickle.dumps(now1)
now2 = pickle.loads(pickled)
print(now1)
print(now2)
'''


'''
import pickle
class Tiny():
    def __str__(self):
        return 'tiny'

obj1 = Tiny()
print(obj1)
print(str(obj1))

pickled = pickle.dumps(obj1)
print(pickled)

obj2 = pickle.loads(pickled)
print(obj2)
'''



import sqlite3
conn = sqlite3.connect('entreprise.db')
curs = conn.cursor()
#curs.execute('''CREATE TABLE zoo
#critter VARCHAR(20) PRIMARY KEY,
#count INT,
#damages FLOAT)''')

curs.execute('INSERT INTO zoo VALUES("duck", 5, 0.0)')
curs.execute('INSERT INTO zoo values ("bear", 2, 1000)')

ins = 'INSERT INTO zoo (critter, count, damages) VALUES(?, ?, ?)'
curs.execute(ins, ('weasel', 1, 2000))


curs.execute('SELECT * FROM zoo')
rows = curs.fetchall()
print(rows)

curs.execute('SELECT * FROM zoo ORDER BY count')
rows2 = curs.fetchall()
print(rows2)

curs.execute('SELECT * FROM zoo ORDER BY count DESC')
rows3 = curs.fetchall()
print(rows3)

curs.execute('''SELECT * FROM zoo WHERE
    damages = (SELECT MAX(damages) FROM zoo)''')
rows4 = curs.fetchall()
print(rows4)

curs.close()
conn.close()









































































































