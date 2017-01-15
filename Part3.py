pythons = {
    'Chapman' : 'Graham',
    'Cleese' : 'John',
    'Idle' : 'Eric',
    'Jones': 'Terry',
    'Palin': 'Michael',
    }

pythons['Gilliam'] = 'Gerry'
pythons['Gilliam'] = 'Terry'

others = {'Marx' : 'Groucho', 'Howard' : 'Moe'}

pythons.update(others)

del pythons['Marx']
del pythons['Howard']

a = pythons.get('Marx', 'Not A Python')

signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}

"""
print(list(signals.keys()))
print(list(signals.values()))
print(list(signals.items()))
"""

save_signals = signals
signals['blue'] = 'confuse everyone'
#print(save_signals)

signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
original_signals = signals.copy()
signals['blue'] = 'confuse everyone'
#print(signals)

#print(original_signals)

empty_set = set()
#print(empty_set)

even_numbers = {0, 2, 4, 6, 8}
#print(even_numbers)
odd_numbers = {1, 3, 5, 7, 9}
#print(odd_numbers)

#print(set('letters'))

#print(set(['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon']))

#print(set(('Ummaguuma', 'Echoes', 'Atom Heart Mother')))

#print(set({'apple': 'red', 'orange': 'orange', 'cherry': 'red'}))

drinks = {
    'martini': {'vodka', 'vermouth'},
    'black russian': {'vodka', 'kahlua'},
    'white russian': {'cream', 'kahlua', 'vodka'},
    'manhattan': {'rye', 'vermouth', 'bitters'},
    'screwdriver': {'orange juice', 'vodka'}
    }
"""
for name, contents in drinks.items():
    if 'vodka' in contents:
        #print(name)
"""

"""
for name, contents in drinks.items():
    if 'vodka' in contents and not ('vermouth' in contents or
                                    'cream' in contents):
        print(name)
"""

"""
for name, contents in drinks.items():
    if contents & {'vermouth', 'orange juice'}:
        print (name)
"""
"""
for name, contents in drinks.items():
    if 'vodka' in contents and not contents & {'vermouth', 'cream'}:
        print (name)
"""

bruss = drinks['black russian']
wruss = drinks['white russian']

a = {1,2}
b = {2,3}

#print(a&b)
#print(a.intersection(b))

#print(bruss & wruss)

#print(a | b)
#print(a.union(b))

"""
print(a-b)
print(a.difference(b))
print(bruss - wruss)
print(wruss - bruss)
"""

#print(a^b)
#print(bruss^wruss)
#print(a.symmetric_difference(b))

#print(a <= b)
#print(a.issubset(b))

#print(bruss <= wruss)

#print(a<=a)

#print(a<b)
#print(a<a)

#print(bruss < wruss)

#print(a>=b)
#print(wruss>=bruss)

#print(a>b)
#print(wruss>bruss)

marxes =['Groucho', 'Chico', 'Harpo']
pythons = ['Chapman', 'Cleese', 'Gilliam', 'Jones', 'Palin']
stooges = ['Moe', 'Curly', 'Larry']
tuple_of_lists = marxes, pythons, stooges
#print(tuple_of_lists)

list_of_lists = [marxes, pythons, stooges]
#print(list_of_lists)

dict_of_lists = {'Marxes': marxes, 'Pythons': pythons, 'Stooges': stooges}
#print(dict_of_lists)

houses = {
    (44.79, -93.14, 284): "My House",
    (38.89, -77.03, 13): "The White House"}
#print (houses)

things = ['mozarella', 'cinderella', 'salmonella']

things[1]=things[1].capitalize()
things[0]=things[0].capitalize()
del things[2]
#print(things)

surprise = ['Groucho', 'Chico', 'Harpo']

surprise[2] = surprise[2].lower()
#print(surprise)
surprise[2] = surprise[2].swapcase()
#print(surprise)

e2f = {
    'dog': 'chien',
    'cat': 'chat',
    'walrus': 'morse'}
#print(e2f['walrus'])
#print(e2f.items())
f2e=e2f.copy()
f2e=list(f2e.items())
a = list(f2e[0])
b = list(f2e[1])
c = list(f2e[2])
temp =a[0]
a[0]=a[1]
a[1]=temp
temp = b[0]
b[0] = b[1]
b[1] = temp
temp = c[0]
c[0] = c[1]
c[1] = temp
#print(a)
d=[]
d.append(a)
d.append(b)
d.append(c)
d=dict(d)
#print(d)
f2e=d
#print(f2e)
#print(f2e['chien'])
#print(f2e.values())

top_cats = ['Henry', 'Grumpy', 'Lucy']
animals = {
    'cats': top_cats,
    'ocpopi':'',
    'emus':'',
    }
life = {
    'animals': animals,
    'plants':'',
    'other':'',
    }
print(life['animals'])
print(life['animals']['cats'])
