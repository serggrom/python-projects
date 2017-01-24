
"""
class Person():
    pass
someone = Person()
"""

"""
class Person():
    def __init__(self):
        pass
"""

"""
class Person():
    def __init__(self, name):
        self.name = name

hunter = Person('Elmer Fudd')

print('The mighty hunter:', hunter.name)
"""

"""
class Car():
    def exclaim(self):
        print("I'm a Car")

class Yugo(Car):
    pass

give_me_a_car = Car()
give_me_a_yugo = Yugo()

give_me_a_car.exclaim()
give_me_a_yugo.exclaim()
"""

"""
class Car():
    def exclaim(self):
        print("I'm a Car!")

class Yugo():
    def exclaim(self):
        print("I'm a Yugo! Much Like a Car,"
              " but more Yugo-ish.")

give_me_a_car = Car()
give_me_a_yugo = Yugo()

give_me_a_car.exclaim()
give_me_a_yugo.exclaim()
"""

"""
class Person():
    def __init__(self, name):
        self.name = name

class MDPerson(Person):
    def __init__(self, name):
        self.name = "Doctor " + name

class JDPerson(Person):
    def __init__(self, name):
        self.name = name + ', Esquire'


person = Person('Fudd')
doctor = MDPerson('Fudd')
lawyer = JDPerson('Fudd')


print(person.name)
print(doctor.name)
print(lawyer.name)
"""

"""
class Car():
    def exclaim(self):
        print("I'm a Car!")

class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo! Much like a Car,"
              " but more Yugo-ish.")
    def need_a_push(self):
        print("A little help here?")

give_me_a_car = Car()
give_me_a_yugo = Yugo()

give_me_a_yugo.need_a_push()
give_me_a_car.need_a_push()
"""

class Person():
    def __init__(self, name):
        self.name = name

"""
class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email

bob = EmailPerson('Bob Frapples', 'bob@frapples.com')

print(bob.name)
print(bob.email)
"""

"""
class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    def get_name(self):
        print('inside the getter')
        return self.hidden_name
    def set_name(self,input_name):
        print('inside the setter')
        self.hidden_name = input_name
    name = property(get_name, set_name)


fowl = Duck('Howard')
fowl.name
print(fowl.get_name())

fowl.name = 'Daffy'
print(fowl.set_name('Daffy'))
"""

"""
class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    @property
    def name(self):
        print('inside the getter')
        return self.hidden_name
    @name.setter
    def name(self,input_name):
        print('inside the setter')
        self.hidden_name = input_name

fowl = Duck('Howard')
print(fowl.name)
fowl.name = 'Donald'
print(fowl.name)
"""

"""
class Circle():
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return 2 * self.radius

c = Circle(5)
print(c.radius)
print(c.diameter)

c.radius = 7
print(c.diameter)

c.diameter = 20
"""

"""
class Duck():
    def __init__(self, input_name):
        self.__name = input_name
    @property
    def name(self):
        print('inside the getter')
        return self.__name
    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.__name =input_name


fowl = Duck('Howard')
print(fowl.name)
fowl.name = 'Donald'
print(fowl.name)

print(fowl._Duck__name)
"""

"""
class A():
    count = 0
    def __init__(self):
        A.count += 1
    def exclaim(self):
        print("I'm an A!")
    @classmethod
    def kids(cls):
        print("A has", cls.count, "little objects")



easy_a = A()
breezy_a = A()
wheezy_a = A()
A.kids()


class CoyoteWeapon():
    @staticmethod
    def commercial():
        print('This CoyoteWeapon has been broght to'
              'you by Acme')

CoyoteWeapon.commercial()
"""


"""
class Quote():
    def __init__(self,person, words):
        self.person = person
        self.words = words
    def who(self):
        return self.person
    def says(self):
        return  self.words + '.'

class QuestionQuote(Quote):
    def says(self):
        return self.words + '?'

class ExclamationQuote(Quote):
    def says(self):
        return self.words + "!"



hunter = Quote('Elmer Fudd', "I'm a hunting wabbits")
print(hunter.who(), 'says:', hunter.says())

hunted1 = QuestionQuote('Bugs Bunny', "What's up, doc")
print(hunted1.who(), 'says:', hunted1.says())

hunted2 = ExclamationQuote('Daffy Duck', "It's a rabbit"
                                         " season")
print(hunted2.who(), 'says:', hunted2.says())


class BabbingBrook():
    def who(self):
        return 'Brook'
    def says(self):
        return 'Babbie'

brook = BabbingBrook()


def who_says(obj):
    print(obj.who(), 'says', obj.says())

who_says(hunter)
who_says(hunted1)
who_says(hunted2)

who_says(brook)
"""

"""
class Word():
    def __init__(self, text):
        self.text = text

    def equals(self, word2):
        return self.text.lower() == word2.text.lower()



first = Word('ha')
second = Word('HA')
third = Word('eh')

print(first.equals(second))
print(first.equals(third))
"""

"""
class Word():
    def __init__(self,text):
        self.text = text
    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()
    def __str__(self):
        return self.text

first = Word('ha')
second = Word('HA')
third = Word('eh')

print(first == second)
print(second == third)

print(first)
"""

"""
class Bill():
    def __init__(self, description):
        self.description = description

class Tail():
    def __init__(self,length):
        self.length = length


class Duck():
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail
    def about(self):
        print('This duck has a', bill.description, 'bill and a', tail.length, 'tail')


tail = Tail('long')
bill = Bill('wide orange')
duck = Duck(bill, tail)
duck.about()
"""

"""

from collections import namedtuple
Duck = namedtuple('Duck', 'bill tail')
duck = Duck('wide orange', 'long')
print(duck)

Duck(bill='wide orange', tail='long')
print(duck.bill)
print(duck.tail)

parts = {'bill': 'wide orange', 'tail': 'long'}
duck2 = Duck(**parts)
print(duck2)

duck3 = duck2._replace(tail='magnificent', bill='crushing')
print(duck3)

duck_dict = {'bill': 'wide orange', 'tail': 'long'}
print(duck_dict)


duck_dict['color'] = 'green'
print(duck_dict)


#duck.color = 'green'
"""


class Thing():
    pass

print(Thing())

example = Thing()

print(example)


class Thing2():
    letters = 'abc'

print(Thing2.letters)


class Thing3():
    letters = 'xyz'

print(Thing3.letters)


class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def dump(self):
        print('Element has name:', self.name, 'and symbol:', self.symbol, 'and number'
             ':', self.number )
    def __str__(self):
        print('Element has name:', self.name, 'and symbol:', self.symbol, 'and number'
             ':', self.number)

hydrogen = Element('Hydrogen', 'H', 1)
print(hydrogen.name)

hydro_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number':1}
hydrogen2 = Element(hydro_dict['name'], hydro_dict['symbol'], hydro_dict['number'])

print(hydrogen2.name)

hydrogen3 = Element(**hydro_dict)
print(hydrogen3.symbol)

hydrogen.dump()
#print(hydrogen2)


class Element2():
    def __init__(self, input_name, input_symbol, input_number):
        self.hidden_name = input_name
        self.hidden_symbol = input_symbol
        self.hidden_number = input_number
    @property
    def name(self):
        return self.hidden_name
    @property
    def symbol(self):
        return self.hidden_symbol
    @property
    def number(self):
        return self.hidden_number




hydrogen_hidden = Element('Hydrogen2', 'H', 1)

print(hydrogen_hidden.name)
print(hydrogen_hidden.symbol)
print(hydrogen_hidden.number)



class Bear():
    def eats(self):
        return 'berries'

class Rabbit():
    def eats(self):
        return 'clover'

class Octothorpe():
    def eats(self):
        return 'campers'


bear = Bear()
rabbit = Rabbit()
octothorpe = Octothorpe()

print(bear.eats())
print(rabbit.eats())
print(octothorpe.eats())



class Laser():
    def does(self):
        return 'desintegrate'

class Claw():
    def does(self):
        return 'crush'

class Smartphone:
    def does(self):
        return 'ring'


class Robot(Laser, Claw, Smartphone):
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone = Smartphone()
    def does(self):
        return '''I have many attachments:
        My laser, to %s.
        My Claw, to %s.
        My Smartphone, to %s''' % (
            self.laser.does(),
            self.claw.does(),
            self.smartphone.does() )

r = Robot()
print(r.does())































