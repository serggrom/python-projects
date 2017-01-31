poem = '''There was a young lady named Bright,
Whose speed was far faster then light:
She started one day
In a relative way,
And returned on the previous night.'''

'''
print(len(poem))

fout = open('relativity', 'wt')
'''

# fout.write(poem)
# print(poem, file=fout)
# print(poem, file=fout, sep='', end='')
# fout.close()
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

# fout = open('relativity', 'xt')
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

"""
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
"""


"""
import sqlalchemy as sa
conn = sa.create_engine('sqlite3://')

conn.execute('''CREATE TABLE zoo
(critter VARCHAR(20) PRIMARY KEY,
count INT,
damage FLOAT)''')

ins = 'INSERT INTO zoo (critter, count, damages) VALUES (?, ?, ?)'

conn.execute(ins, 'duck', 10, 0.0)
conn.execute(ins, 'bear', 2, 1000.0)
conn.execute(ins, 'weasel', 1, 2000.0)

rows = conn.execute('SELECT * FROM zoo')

for row in rows:
    print(row)
"""

'''
import sqlalchemy as sa
from sqlalchemy.ext.declarative import  declarative_base

conn = sa.create_engine('sqlite:///zoo.db')

Base = declarative_base()

class Zoo(Base):
    __tablename__ = 'zoo'
    critter = sa.Column('critter', sa.String, primary_key=True)
    count = sa.Column('count', sa.Integer)
    damages = sa.Column('damages', sa.Float)
    def __init__(self, critter, count, damages):
        self.critter = critter
        self.count = critter
        self.damages = damages
    def __repr__(self):
        return "<Zoo({}, {}, {})>".format(self.critter, self.count, self.damages)

Base.metadata.create_all(conn)

first = Zoo('duck', 10, 0.0)
second = Zoo('bear', 2, 1000.0)
third = Zoo('weasel', 1, 2000.0)
print(first)



from sqlalchemy.orm import sessionmaker
Session = sessionmaker(blind=conn)
session = Session()
session.add(first)
session.add_all([second, third])
session.commit()
'''


'''
import dbm
db = dbm.open('definitions', 'c')

db['mustard'] = 'yellow'
db['ketchup'] = 'red'
db['pesto'] = 'green'

print(len(db))

db.close()

db = dbm.open('definitions', 'r')
print(db['mustard'])
'''


'''
import memcache
db = memcache.Client(['127.0.0.1:11211'])

db.set('marco', 'polo')
db.get('marco')
db.set('ducks', 0)
db.get('ducks')
'''

'''
import redis
conn = redis.Redis()

conn.keys('*')
'''


'''
test1 = 'This is a test of the emergency text system'

fout = open('test.txt', 'wt')
fout.write(test1)

fout.close()

fin = open('test.txt', 'rt')
test2 = fin.read()
print(test2)
'''


import csv


"""
book_csv = [{'author': 'J R R Tolkien', 'book': 'The Hobbit'},
            {'author': 'Lyne Truss', 'book': '"Eats, Shoots & Leaves"'}]
with open('book', 'wt') as fout:
    cout = csv.DictWriter(fout, ['book', 'author'])
    cout.writeheader()
    cout.writerows(book_csv)

print(book_csv)





with open('book', 'rt') as fin:
    cin = csv.DictReader(fin)
    books = [row for row in cin]

print(books)
"""

book_csv2 = [ ['The Weirdstone of Brisingame', 'Alan Garner', '1960'],
             ['Perdido Streer Station', 'China Mieville', '2000'],
             ['Thud!', 'Terry Pratchett', '2005'],
              ['The Spellman Files', 'Lisa Lutz', '2007'],
              ['Small Gods', 'Terry Pratchett', '1992']]
with open('books', 'wt') as fout:
    csvout = csv.writer(fout)
    csvout.writerows(book_csv2)


with open('books', 'rt') as fin:
    cin = csv.DictReader(fin, fieldnames=['title', 'author', 'year'])
    book_csv2 = [row for row in cin]

print(book_csv2)



with open('books', 'wt') as fout:
    cout = csv.DictWriter(fout, ['title', 'author', 'year'])
    cout.writeheader()
    cout.writerows(book_csv2)



import sqlite3


conn = sqlite3.connect('books.db')
curs = conn.cursor()
#curs.execute('''CREATE TABLE book
#(title TEXT,
#author TEXT,
#year INT)''')
conn.commit()



ins_str = 'INSERT INTO book VALUES(?, ?, ?)'
with open('books', 'rt') as infile:
    books = csv.DictReader(infile)
    for book in books:
        curs.execute(ins_str, (book['title'], book['author'], book['year']))



query = 'SELECT title FROM book ORDER BY title ASC'
for row in curs.execute(query):
    print(row)



query2 = '''SELECT title FROM book ORDER BY
 case when (title like "The %") then substr(title,5) else title end'''
for row in curs.execute(query2):
    print(row[0])


query3 = 'SELECT * FROM book ORDER BY year'
for row in curs.execute(query3):
    print(row)














































