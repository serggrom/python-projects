"""

import unicodedata
def unicode_test(value):
    import unicodedata
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print('value = "%s", name = "%s", value2 = "%s"' % (value, name, value2))

unicode_test('A')
unicode_test('Я')
unicode_test('$')
unicode_test('\u00a2')
unicode_test('\u2603')

place = 'café'
print(place)

unicode_test('é')
unicode_test('e')
print(unicodedata.name('\u00e9'))
print(unicodedata.lookup('LATIN SMALL LETTER E WITH ACUTE'))

place2 = 'caf\u00e9'
print(place2)

place3 = 'caf\N{LATIN SMALL LETTER E WITH ACUTE}'
print(place3)


u_umlaut = '\N{LATIN SMALL LETTER U WITH DIAERESIS}'
print(u_umlaut)

drink = 'Gew' + u_umlaut + 'rztraminer'

print('Now I can finally have my', drink, 'in a', place)

print(len('$'))
print(len('\U0001f47b'))

snowman = '\u2603'
print(len(snowman))

ds = snowman.encode('utf-8')
print(len(ds))
print(ds)

ds2 = snowman.encode('ascii', 'replace')
print(ds2)

ds3 = snowman.encode('ascii', 'ignore')
print(ds3)

ds4 = snowman.encode('ascii', 'backslashreplace')
print(ds4)

ds5 = snowman.encode('ascii', 'xmlcharrefreplace')
print(ds5)

place4 = 'caf\u00e9'
print(place4)

print(type(place4))

place_byte = place4.encode('utf-8')
print(place_byte)
print(type(place_byte))
place4 = place_byte.decode('utf-8')
#place4 = place_byte.decode('ascii')
place4 = place_byte.decode('latin-1')
print(place4)
place4 = place_byte.decode('windows-1252')
print(place4)
"""

"""
actor = 'Richard Gere'
cat = 'Chester'
weight = 28

print("My wife's favorite actor is %s" % actor)
print("Our cat %s weights %s pounds" % (cat, weight))

n = 42
f = 7.03
s = 'string cheese'

print('%d %f %s' % (n, f, s))


print('%10d %10f %10s' % (n, f, s))
print('%-10d %-10f %-10s' % (n, f, s))
print('%10.4d %10.4f %10.4s' % (n, f, s))
print('%.4d %.4f %.4s' % (n, f, s))
print('%*.*d %*.*f %*.*s' % (10, 4, n, 10, 4, f, 10, 4, s))
print('{} {} {}'.format(n, f, s))
print('{2} {0} {1}'.format(f, s, n))
print('{n} {f} {s}'.format(n=42, f=7.03, s='string cheese'))

d = {'n': 42, 'f': 7.03, 's': 'string cheese'}

print('{0[n]} {0[f]} {0[s]} {1}'.format(d, 'other'))

print('{0:d} {1:f} {2:s}'.format(n, f, s))

print('{n:d} {f:f} {s:s}'.format(n=42, f=7.03, s='string cheese'))

print('{0:10d} {1:10f} {2:10s}'.format(n,f,s))

print('{0:>10d} {1:>10f} {2:>10s}'.format(n, f, s))

print('{0:<10d} {1:<10f} {2:<10s}'.format(n, f, s))

print('{0:^10d} {1:^10f} {2:^10s}'.format(n, f, s))


print('{0:>10d} {1:>10.4f} {2:>10.4s}'.format(n, f, s))

print('{0:!^20s}'.format('BIG SALE'))
"""


import re

result = re.match('You', 'Young Frankenstein')

youPattern = re.compile('You')

result2 = youPattern.match('Young Frankenstein')


source = 'Young Frankenstein'

"""
m = re.match('You', source)
if m:
    print(m.group())

m = re.match('^You', source)
if m:
    print((m.group()))

m = re.match('Frank', source)
if m:
    print(m.group())

m = re.search('Frank', source)
if m:
    print(m.group())

m = re.match('.*Frank', source)
if m:
    print(m.group())
"""


"""
m = re.findall('n', source)
print(m)
print('Found', len(m), 'matches')

m = re.findall('n.', source)
print(m)

m = re.findall('n.?', source)
print(m)
"""

"""
m = re.split('n', source)
print(m)

m = re.sub('n', '?', source)
print(m)
"""

import string
printable = string.printable

"""
print(len(printable))
print(printable[0:50])
print(printable[50:])

print(re.findall('\d', printable))

print(re.findall('\w', printable))

print(re.findall('\s', printable))

x = 'abc' + '-/*' + '\u00ea' + '\u0115'

print(re.findall('\w', x))
"""


source2 = '''I wish I may, I wish I might
Have a dish of fish tonight.'''

"""
print(re.findall('wish', source2))

print(re.findall('wish|fish', source2))

print(re.findall('^wish', source2))

print(re.findall('^I wish', source2))

print(re.findall('fish$', source2))

print(re.findall('fish tonight.$', source2))

print(re.findall('fish tonight\.$', source2))

print(re.findall('[wf]ish', source2))

print(re.findall('[whs]+', source2))

print(re.findall('ght\W', source2))

print(re.findall('I (?=wish)', source2))

print(re.findall('\bfish', source2))

print(re.findall(r'\bfish', source2))
"""



"""
m = re.search(r'(. dish\b).*(\bfish)', source2)
print(m.group())

m = re.search(r'(?P<DISH>. dish\b).*(?P<FISH>\bfish)', source2)

print(m.group())
print(m.groups())
print(m.group('DISH'))
print(m.group('FISH'))

blist = [1, 2, 3, 255]

the_bytes = bytes(blist)
print(the_bytes)
the_byte_array = bytearray(blist)
print(the_byte_array)

print(b'\x61')
print(b'\x01abc\xff')

#the_bytes[1] = 127

the_byte_array[1] = 127

print(the_byte_array)

the_bytes = bytes(range(0, 256))
the_byte_array = bytearray(range(0, 256))
print(the_bytes)
"""

"""
import struct

valid_png_header = b'\x89PNG\r\n\x1a\n'
data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR' + \
    b'\x00\x00\x00\x9a\x00\x00\x00\x8d\x08\x02\x00\x00\x00\xc0'

if data[:8] == valid_png_header:
    width, height = struct.unpack('>LL', data[16:24])
    print('Valid PNG, width', width, 'height', height)
else:
    print('Not a valid PNG')

print(data[16:20])

print(data[20:24])

print(0x9a)
print(0x8d)

print(struct.pack('>L', 154))
print(struct.pack('>L', 141))

print(struct.unpack('>2L', data[16:24]))
print(struct.unpack('>16x2L6x', data))
"""

"""
import binascii
valid_png_header = b'\x89PNG\r\n\x1a\n'
print(binascii.hexlify(valid_png_header))
print(binascii.unhexlify(binascii.hexlify(valid_png_header)))
"""

import unicodedata

mystery = '\U0001f4a9'

print(mystery)
print(unicodedata.name(mystery))

pop_bytes = mystery.encode('utf-8')
print(pop_bytes)

pop_string = pop_bytes.decode('utf')
print(pop_string)

roast = 'roast beef'
ham = 'ham'
head = 'head'
clam = 'clam'

print('My kitty cat likes %s\n'
      'My kitty cat likes %s\n'
      'My kitty cat fell on %s\n'
      'And now thinks he is %s' % (roast, ham, head, clam))



letter = '''Dear {salutation} {name},
Thank you for your letter. We are sorry that our {product} {verbed} in your
{room}. Please note that it should never be used in a {room}, especially
near any {animals}.
Send us your receipt and {amount} for shipping and handling. We will send
you another {product} that, in our tests, is {percent}% less likely to
have {verbed}.
Thank you for your support.
Sincerely,
{spokesman}
{job_title}'''


response = {
    'salutation': 'customer',
    'name': 'John',
    'product': 'phone',
    'verbed': 'placed',
    'room': 'home',
    'animals': 'cats',
    'amount': 'one hundred',
    'percent': '95',
    'spokesman': 'retail man',
    'job_title': 'CEO'
}

print(letter.format(**response))


import re
mammoth = '''
We have seen thee, queen of cheese,
Lying quietly at your ease,
Gently fanned by evening breeze,
Thy fair form no flies dare seize.
All gaily dressed soon you'll go
To the great Provincial show,
To be admired by many a beau
In the city of Toronto.
Cows numerous as a swarm of bees,
Or as the leaves upon the trees,
It did require to make thee please,
And stand unrivalled, queen of cheese.
May you not receive a scar as
We have heard that Mr. Harris
Intends to send you off as far as
The great world's show at Paris.
Of the youth beware of these,
For some of them might rudely squeeze
And bite your cheek, then songs or glees
We could not sing, oh! queen of cheese.
We'rt thou suspended from balloon,
You'd cast a shade even at noon,
Folks would think it was the moon
About to fall and crush them soon.
'''

print(re.findall(r'\bc\w*', mammoth))

print(re.findall(r'\bc\w{3}\b', mammoth))

print(re.findall(r'\b\w*r\b', mammoth))

print(re.findall(r'\b\w*[aieou]{3}[^aieou\s]*\w*\b', mammoth))

import binascii
import struct
gif = bytes(binascii.unhexlify(b'47494638396101000100800000000000ffffff21f9') +
            binascii.unhexlify(b'0401000000002c000000000100010000020144003b'))
print(gif)


if gif[:6] == b'GIF89a':
    print('True gif')
    width, height = struct.unpack('<2H', gif[6:10])
    print(width, height)
    print(gif[6:8])
    print(gif[8:10])















































