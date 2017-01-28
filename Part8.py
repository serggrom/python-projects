
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


bdata = bytes(range(0, 256))
print(len(bdata))

fout = open('bfile', 'wb')
fout.write(bdata)
fout.close()

fout = open













































































































































