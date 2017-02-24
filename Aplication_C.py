import math

'''
print(math.pi)
print(math.e)
print(math.fabs(-256))

print(math.floor(105.6))
print(math.floor(-105.6))

print(math.ceil(105.6))
print(math.ceil(-105.6))

print(math.factorial(8))

print(math.log(math.e))
print(math.log(8, 2))

print(math.sqrt(100))

x = 3
y = 4
print(math.hypot(x, y))

print(math.radians(180))
print(math.degrees(math.pi))

print(1j * 1j)

print((7 + 1j) * 1j)
'''

'''
from decimal import Decimal
price = Decimal('19.99')
tax = Decimal('0.06')
total = price + (price * tax)
print(total)


penny = Decimal('0.01')
print(total.quantize(penny))
'''

'''
from fractions import Fraction
a = Fraction(1, 3) * Fraction(2, 3)
print(a)

print(Fraction(1.0/3.0))
print(Fraction(Decimal('1.0')/Decimal('3.0')))

import fractions
print(fractions.gcd(24, 16))
'''

import numpy as np

'''
#b = np.array([2, 4, 6, 8])
#print(b.shape)


a = np.arange(10)
#print(a.ndim)

b = np.arange(7, 11, 2)
#print(b)

g = np.arange(10, 4, -1.5, dtype=np.float)
print(g)
'''

'''
a = np.zeros((3,))
print(a.ndim)

b = np.zeros((2, 4))
print(b.shape)

k = np.ones((3, 5))
print(k)

m = np.random.random((3, 5))
print(m)
'''

'''
a = np.arange(10)
print(a)

a = a.reshape(2, 5)
print(a.size)

a = a.reshape(5, 2)
print(a.shape)

a.shape = (2, 5)
print(a)
'''

'''
a = np.arange(10)
print(a[-1])
a.shape = (2, 5)
print(a[1,2])
'''

'''
a = np.arange(10)
a = a.reshape(2, 5)
print(a)
print(a[0, 2:])
print(a[-1, :3])

a[:, 2:4] = 1000
print(a)
'''

'''
from numpy import *
a = arange(4)
print(a)
a *= 3
print(a)


plain_list = list(range(4))
print(plain_list)
plain_list = [num * 3 for num in plain_list]
print(plain_list)
'''

'''
from numpy import *
a = zeros((2, 5)) + 17.0
print(a)
'''


import numpy as np

coefficients = np.array([[4, 5], [1, 2]])
dependents = np.array([20, 13])
answers = np.linalg.solve(coefficients, dependents)
print(answers)
print(4 * answers[0] + 5 * answers[1])
print(1 * answers[0] + 2 * answers[1])
product = np.dot(coefficients, answers)
print(product)

truth = np.allclose(product, dependents)
print(truth)


















































