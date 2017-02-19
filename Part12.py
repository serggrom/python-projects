'''
def ftoc(f_temp):
    "Convert Fahrenheit temperature <f_temp> to Celsius and return it."
    f_boil_temp = 212.0
    f_freeze_temp = 32.0
    c_boil_temp = 100.0
    c_freeze_temp = 0.0
    f_range = f_boil_temp - f_freeze_temp
    c_range = c_boil_temp - c_freeze_temp
    f_c_ratio = c_range / f_range
    c_temp = (f_temp - f_freeze_temp) * f_c_ratio + \
             c_freeze_temp
    return c_temp
#if __name__ == "__main__":
for f_temp in [-40.0, 0.0, 32.0, 100.0, 212.0]:
    c_temp = ftoc(f_temp)
    print('%f F => %f C' % (f_temp, c_temp))
'''

'''
F_BOIL_TEMP = 212.0
F_FREEZE_TEMP = 32.0
C_BOIL_TEMP = 100.0
C_FREEZE_TEMP = 0.0
F_RANGE = F_BOIL_TEMP - F_FREEZE_TEMP
C_RANGE = C_BOIL_TEMP - C_FREEZE_TEMP
F_C_RATIO = C_RANGE/ F_RANGE
def ftoc(f_temp):
    "Convert Fahrenheit temparature <f_temp> to Celsius and return it."
    c_temp = (f_temp - F_FREEZE_TEMP) * F_C_RATIO + C_FREEZE_TEMP
    return c_temp
for f_temp in [-40.0, 0.0, 32.0, 100.0, 212.0]:
    c_temp = ftoc(f_temp)
    print('%f F => %f C' % (f_temp, c_temp))
'''

'''
a = 1
b = 2
c = 3
print(a)
print(b)
print(c)
'''


"Module docstring here"

'''
def func():
    "Function docstring here."
    first = 1
    second = 2
    third = 3
    print(first)
    print(second)
    print(third)
func()
'''

'''
def just_do_it(text):
    """
    >>> just_do_it('duck')
    'Duck'
    >>> just_do_it('a veritable flock of ducks')
    'A Veritable Flock Of Ducks'
    >>> just_do_it("I'm fresh out of ideas")
    "I'm Fresh Out Of Ideas"
    """
    from string import capwords
    return capwords(text)
if __name__ == '__main__':
    import doctest
    doctest.testmod()
'''

def dump(func):
    "Print input arguments and output value(s)"
    def wrapped(*args, **kwargs):
        print("Function name: %s" % func.__name__)
        print("Input arguments: %s" % ' '.join(map(str, args)))
        print("Input keywords: %s" % kwargs.items())
        output = func(*args, **kwargs)
        print("Output: ", output)
        return output
    return wrapped

'''
def process_cities(filename):
    with open(filename, 'rt') as file:
        for line in file:
            line = line.strip()
            if 'quit' in line.lower():
                return
            country, city = line.split()
            city = city.strip()
            country = country.strip()
            print(city.title(), country.title(), sep=',')
if __name__ == '__main__':
    import sys
    process_cities(sys.argv[1])
'''

'''
import logging
logging.basicConfig(level=logging.DEBUG)
logging.debug("Looks like rain")
logging.info("And hail")
logging.warn("Did i hear thunder?")
logging.error("Was that lightning?")
logging.critical("Stop fencing and getinside!")
'''

'''
import logging
logging.basicConfig(level='DEBUG')
logger = logging.getLogger('bunyan')
logger.debug('Timber!')
'''


'''
import logging
logging.basicConfig(level='DEBUG', filename='blue_ox.log')
logger = logging.getLogger('bunyan')
logger.debug("Where's my axe?")
logger.warn("I need my axe")
'''

'''
import logging
fmt = '%(asctime)s %(levelname)s %(lineno)s %(message)s'
logging.basicConfig(level='DEBUG', format=fmt)
logger = logging.getLogger('bunyan')
logger.error("Where's my other plaid shirt?")
'''

'''
from time import time, sleep
t1 = time()
num = 5
num *= 2
sleep(1.0)
print(time() - t1)
'''

'''
from timeit import timeit
print(timeit('num = 5; num*= 2', number=1))
'''

'''
from timeit import repeat
print(repeat('num = 5; num *=2', number=1, repeat=3))
'''

'''
from timeit import timeit
def make_list_1():
    result = []
    for value in range(1000):
        result.append(value)
    return result
def make_list_2():
    result = [value for value in range(1000)]
    return result
print('make_list_1 takes', timeit(make_list_1, number=1000000), 'seconds')
print('make_list_2 takes', timeit(make_list_2, number=1000000), 'seconds')
'''





































































































































































