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


x = 7
"""
print(x==5)
print(x==7)
print(5<x)
print(x<10)
"""

#print(5<x and x>10)
#print(5<x or x>10)
#print(5<x and not x<10)

some_list = []
if some_list:
    print('There is something in here')
else:
    print('Hey, it is empty')

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




