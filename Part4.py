"""
disaster = True
if disaster:
     print ("Woe!")
else:
     print('Whee!')


furry = True
small = True
if furry:
    if small:
        print('It is a cat')
    else:
        print('It is a bear')
else:
    if small:
        print('It is a skink')
    else:
        print('It is a human. Or hairless bear')


color = 'puce'
if color == 'red':
    print('It is a tomato')
elif color == 'green':
    print('It is a green peper')
elif color == 'bee purple':
    print('I dont now what is it. but only bees can see it')
else:
    print('Ive never heard of the color', color)
"""

"""
x = 7

print(x==5)
print(x==7)
print(5<x)
print(x<10)
"""
"""
#print(5<x and x>10)
#print(5<x or x>10)
#print(5<x and not x<10)

some_list = []
if some_list:
    print('There is something in here')
else:
    print('Hey, it is empty')
"""

""""
count = 1
while count <=5:
    #print (count)
    count+=1
"""


"""
while True:
    stuff = input("String to capitalize [type q to quit]:")
    if stuff == 'q':
        break
    print (stuff.capitalize())
"""

"""
while True:
     value = input('Integer, please [q to quit]: ')
     if value == 'q':
          break
     number = int(value)
     if number % 2 == 0:
          continue
     print(number, 'squared is', number*number)
"""

"""
numbers = [1,3,5]
position=0
while position < len(numbers):
     number = numbers[position]
     if number % 2 ==0:
          print('Found even number',number)
     position +=1
else:
     print('No even number found')
"""

"""
rabbits = ['Flopsy', 'Mopsy', 'Cottonial', 'Peter']
current = 0
while current < len(rabbits):
     print(rabbits[current])
     current +=1
"""

"""
rabbits = ['Flopsy', 'Mopsy', 'Cottonial', 'Peter']
for rabbit in rabbits:
     print(rabbit)
"""

"""
word = 'cat'
for letter in word:
     print(letter)
"""


accusation = {'room': 'ballroom', 'weapon': 'lead pipe',
              'person': 'Col.Mustard'}

"""
for card in accusation:
     print(card)

for value in accusation.values():
     print(value)
"""

"""
for item in accusation.items():
     print(item)
"""

"""
for card, contents in accusation.items():
     print('Card', card, 'has the contents', contents)
"""

"""
cheeses = []
for cheese in cheeses:
     print('This shop has some lovely', cheese)
     break
else:
     print('This is not much of a cheese shop, is it?')
"""

"""
cheeses = []
found_one = False
for cheese in cheeses:
     found_one = True
     print('This shop has some lovely', cheese)
     break
if not found_one:
     print('This is not a much of cheese shop, is it?')
"""

"""
days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
     print(day, ': drink', drink, '- eat', fruit, '- enjoy', dessert)
"""

"""
english = 'Monday', 'Tuesday', 'Wednesday'
french = 'Lundi', 'Mardi', 'Mercedi'

print(list(zip(english, french)))
print(dict(zip(english, french)))
"""

"""
for x in range(0,3,):
     print(x)

print(list(range(0,3)))

for x in range (2, -1, -1):
     print(x)


print(list(range(2, -1, -1)))

print(list(range(0, 11, 2)))
"""

"""
number_list = []
for number in range(1,6):
     number_list.append(number)
print(number_list)
"""

"""
number_list = list(range(1,6))
print(number_list)
"""

"""
number_list = [number for number in range(1,6)]
print(number_list)
"""

"""
number_list = [number-1 for number in range(1,6)]
print(number_list)
"""

"""
a_list = [number for number in range(1,6) if number % 2 == 1]
print(a_list)
"""

"""
a_list =[]
for number in range(1,6):
     if number % 2 ==1:
          a_list.append(number)
print(a_list)
"""


"""
rows = range(1,4)
cols = range(1,3)
for row in rows:
     for col in cols:
          print(row, col)
"""

"""
rows = range(1,4)
cols = range(1,3)
cells = [(row, col) for row in rows for col in cols]
for cell in cells:
     print(cell)

for row, col in cells:
     print(row, col)
"""

"""
word = 'letters'
letter_counts = {letter: word.count(letter) for letter in word}
print(letter_counts)

lettet_counts = {letter: word.count(letter) for letter in set(word)}
print(letter_counts)
"""

"""
def answer():
    print(42)
answer()


def run_something(func):
    func()
run_something(answer)
"""

"""
def add_args(arg1, arg2):
    print(arg1 + arg2)

print(type(add_args))

def run_something_with_args(func, arg1, arg2):
    func(arg1, arg2)

run_something_with_args(add_args, 5, 9)
"""

"""
def sum_args(*args):
    return sum(args)

def run_with_positional_args(func, *args):
    return func(*args)

print(run_with_positional_args(sum_args, 1, 2, 3, 4))
"""

"""
def outer(a,b):
    def inner(c,d):
        return  c + d
    return inner(a,b)

print(outer(4,7))
"""


"""
def knigths(saying):
    def inner(quote):
        return "We are the knights who say: '%s'" % quote
    return inner(saying)
print(knigths('Ni!'))
"""

"""
def knights2(saying):
    def inner2():
        return "We are the knights who say: '%s'" % saying
    return inner2


a = knights2('Duck')
b = knights2('Hasenpfeffer')
print(type(a))
print(type(b))

print(a)
print(b)
print(a())
print(b())
"""

"""
def edit_story(words, func):
     for word in words:
          print(func(word))


stairs = ['thud', 'meow', 'thud', 'hiss']


def enliven(word):
     return word.capitalize() + '!'

edit_story(stairs, enliven)

edit_story(stairs, lambda word: word.capitalize() + '!')
"""

"""
print(sum(range(1, 101)))
"""

"""
def my_range(first=0, last=10, step=1):
     number = first
     while number < last:
          yield number
          number += step

print(my_range)
ranger = my_range(1,5)
print(ranger)


for x in ranger:
     print (x)
"""


"""
def square_it(func):
     def new_function(*args, **kwargs):
          result = func (*args,**kwargs)
          return result*result
     return new_function

def document_it(func):
     def new_function(*args, **kwargs):
          print('Running function:', func.__name__)
          print('Positional arguments:', args)
          print('Keyword arguments:',kwargs)
          result = func(*args, **kwargs)
          print('Result:', result)
          return result
     return new_function



@document_it
@square_it
def add_ints(a, b):
     return a + b
"""





"""
print(add_ints(3,5))
"""

"""
cooler_add_ints = document_it(add_ints)
cooler_add_ints(3,5)
"""

animal = 'fruitbat'

"""
def print_global():
     print('inside print_global:', animal)

print('at the top level:', animal)
print_global()
"""
"""
def change_and_print_global():
     print('inside chage_and_print_global:', animal)
     global animal
     animal =  'wombat'
     print('after the change:', animal)
change_and_print_global()

def change_local():
     animal = 'wombat'
     print('inside change_local:', animal, id(animal))
     print('locals:', locals())

change_local()

print(id(animal))

print('globals:', globals())
"""



















