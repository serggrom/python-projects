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
































































































