"""
import report
description = report.get_description()
print("Today's weather :", description)
"""

"""
import report as wr
description = wr.get_description()
print("Today's weather:", description)
"""

"""
from report import get_description
description = get_description()
print("Today's weather:", description)
"""

"""
from report import get_description as do_it
description = do_it()
print("Today's weather:", description)
"""

"""
import sys
for place in sys.path:
    print(place)
"""


"""
from weather_example import daily, weekly
print("Daily forecast:", daily.forecast())
print("Weekly forecast:")
for number, outlook in enumerate(weekly.forecast(), 1):
    print(number, outlook)
"""

"""
periodic_table = {'Hydrogen': 1, 'Helium': 2}
print(periodic_table)

carbon = periodic_table.setdefault('Carbon', 12)
print(periodic_table)

helium = periodic_table.setdefault('Helium', 947)

print(periodic_table)
"""



"""
from collections import defaultdict
periodic_table = defaultdict(int)
periodic_table['Hydrogen'] = 1
periodic_table['Lead']
print(periodic_table)
"""

"""
from collections import defaultdict

def no_idea():
    return 'Huh?'

bestiary = defaultdict(no_idea)
bestiary['A'] = 'Abominable Snowman'
bestiary['B'] = 'Basilisk'
print(bestiary['A'])
print(bestiary['B'])
print(bestiary['C'])

bestiary = defaultdict(lambda: 'Huh?')
print(bestiary['C'])
"""

"""
from collections import  defaultdict
food_counter = defaultdict(int)
for food in ['spam', 'spam', 'eggs', 'spam']:
    food_counter[food] += 1
print(food_counter)

for food, count in food_counter.items():
    print(food, count)

dict_counter = {}
for food in ['spam', 'spam', 'eggs', 'spam']:
    if not food in dict_counter:
        dict_counter[food] = 0
    dict_counter[food] += 1
for food, count in dict_counter.items():
    print(food, count)
"""

"""
from collections import Counter
breakfast = ['spam', 'spam', 'eggs', 'spam']
breakfast_counter = Counter(breakfast)
print(breakfast_counter)
print(breakfast_counter.most_common())
lunch = ['eggs', 'eggs', 'bacon']
lunch_counter = Counter(lunch)
print(lunch_counter)
print(breakfast_counter | lunch_counter)
"""

"""
quotes = {
    'Moe': 'A wise guy, huh?',
    'Larry': 'Ow!',
    'Curly': 'Nyuk nyuk!'
}

for stooge in quotes:
    print(stooge)
"""

"""
from collections import OrderedDict
qoutes = OrderedDict([('Moe', 'A wise guy, huh?'),
    ('Larry','Ow!'),
    ('Curly', 'Nyuk nyuk!')])
for stooge in qoutes:
    print(stooge)
"""

"""
def palindrome(word):
    from collections import deque
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True

print(palindrome(''))

def another_palindrome(word):
    return word == word[::-1]

print(another_palindrome('rada'))
"""

"""
import itertools
for item in itertools.chain([1, 2], ['a', 'b']):
    print(item)

for item in itertools.cycle([1, 2]):
    print(item)
"""

"""
import itertools
for item in itertools.accumulate([1, 2, 3, 4]):
    print(item)

def multiply(a, b):
    return a * b

for item in itertools.accumulate([1, 2, 3,4], multiply):
    print(item)
"""

"""
from collections import OrderedDict
from pprint import pprint
quotes = OrderedDict([
    ('Moe', 'A wise guy, huh?'),
    ('Larry', 'Ow!'),
    ('Curly', 'Nyuk nyuk!')
    ])
print(quotes)

pprint(quotes)
"""

"""
import zoo
work = zoo.hours()
print(work)

import zoo as menagerie
work = menagerie.hours()
print(work)

from zoo import hours
print(hours())

from  zoo import hours as info
print(info())
"""


plain = {
    'a': 1,
    'b': 2,
    'c': 3
}

print(plain)


from collections import OrderedDict
fancy = OrderedDict([
    ('a', 1),
    ('b', 2),
    ('c', 3)
])
print(fancy)


from collections import defaultdict
dict_of_list = defaultdict(list)
dict_of_list['a'] = ['something for a']
print(dict_of_list['a'])


























