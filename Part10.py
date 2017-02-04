

'''
fout = open('oops.txt', 'wt')
print('Oops, I created a file', file=fout)
fout.close()
'''

import os


'''
print(os.path.exists('oops.txt'))

print(os.path.exists('./oops.txt'))

print(os.path.exists('waffles'))

print(os.path.exists('.'))

print(os.path.exists('..'))
'''

'''
name = 'oops.txt'

print(os.path.isfile(name))

print(os.path.isdir(name))

print(os.path.isdir('.'))

print(os.path.isabs(name))

print(os.path.isabs('/big/fake/name'))

print(os.path.isabs('big/fake/name'))
'''

import  shutil

'''
shutil.copy('oops.txt', 'ohno.txt')

os.rename('ohno.txt', 'ohwell.txt')
'''

#os.link('oops.txt', 'yikes.txt')
#print(os.path.isfile('yikes.txt'))

'''
print(os.path.islink('yikes.txt'))
os.symlink('oops.txt', 'jeepers.txt')
print(os.path.islink('jeepers.txt'))
'''



#os.chmod('oops.txt', 0o400)


import stat
#os.chmod('oops.txt', stat.S_IRUSR)


'''
uid = 5
gid = 22
os.chown('oops', uid. gid)
'''


#print(os.path.abspath('oops.txt'))

#print(os.path.realpath('jeepers.txt'))

'''
os.remove('ohwell.txt')
print(os.path.exists('ohwell.txt'))
'''

'''
os.mkdir('poems')
print(os.path.exists('poems'))

os.rmdir('poems')
print(os.path.exists('poems'))
'''

'''
os.mkdir('poems')
print(os.listdir('poems'))

os.mkdir('poems/mcintyre')
print(os.listdir('poems'))
'''

"""
fout = open('poems/mcintyre/the_good_man.txt', 'wt')
fout.write('''Cheerful and happy was his mood,
... He to the poor was kind and good,
... And he oft' times did find them food,
... Also supplies of coal and wood,
... He never spake a word was rude,
... And cheer'd those did o'er sorrows brood,
... He passed away not understood,
... Because no poet in his lays
... Had penned a sonnet in his praise,
... 'Tis sad, but such is world's ways.
''')
fout.close()
"""


#print(os.listdir('poems/mcintyre'))

#os.chdir('poems')
#print(os.listdir('.'))

import glob


'''
print(glob.glob('m*'))

print(glob.glob('??'))

print(glob.glob('m??????e'))

print(glob.glob('[klm]*e'))
'''

'''
print(os.getpid())
print(os.getcwd())
'''

import subprocess

'''
ret = subprocess.getoutput('data')
#print(ret)

ret = subprocess.getoutput('date -u | wc')

#ret = subprocess.check_output(['date', '-u'])
print(ret)

ret = subprocess.getstatusoutput('date')

ret = subprocess.call('date')
print(ret)
'''



import multiprocessing



'''
def do_this(what):
    whoami(what)

def whoami(what):
    print("Process %s says: %s" % (os.getpid(), what))
if __name__ == "__main__":
    whoami("I'm the main program")
    for n in range(4):
        p = multiprocessing.Process(target=do_this,
            args= ("I'm a function %s" % n))
        p.start()

'''


import calendar


#print(calendar.isleap(2016))


from datetime import date

'''
halloween = date(2014, 10, 31)
print(halloween)

print(halloween.day)
print(halloween.month)


print(halloween.isoformat())
'''

#now = date.today()
#print(now)

from datetime import timedelta


'''
one_day = timedelta(days=1)

tomorrow = now + one_day
print(tomorrow)

print(now + 17*one_day)

yesterday = now - one_day
print(yesterday)
'''


from datetime import time

noon = time(12, 0, 0)

#print(noon.microsecond)

from datetime import datetime

some_day = datetime(2014, 1, 2, 3, 4, 5, 6)

#print(some_day)

#print(some_day.isoformat())

#now = datetime.now()
#print(now.microsecond)

noon = time(12)
this_day = date.today()
noon_today = datetime.combine(this_day, noon)

#print(noon_today.time())

import time

now = time.time()


#print(now)
#print(time.ctime(now))

#print(time.localtime(now))
#print(time.gmtime(now))



tm = time.localtime(now)

#print(time.mktime(tm))


fmt = "It's %A, %B, %d, %Y, local time %I:%M:%S%p"

t = time.localtime()
#print(t)

print(time.strftime(fmt, t))

some_day = date(2017, 2, 4)
#print(some_day.strftime(fmt))

#from datetime import time
#some_time = time(18, 00)
#print(some_time.strftime(fmt))


#fmt = "%Y-%m-%d"
#print(time.strptime("2017-02-04", fmt))

import locale
from datetime import date


'''
halloween = date(2017, 10, 31)
for lang_country in ['en_us', 'fr_fr', 'de_de', 'es_es',
                     'is_is']:
    locale.setlocale(locale.LC_TIME, lang_country)
    halloween.strftime('%A, %B %d')
'''



names = locale.locale_alias.keys()
#print(names)

good_names = [name for name in names if \
              len(name) == 5 and name[2] == '_']

#print(good_names[:5])

de = [name for name in good_names if name.startswith('de')]
#print(de)




'''
fout = open('today.txt', 'wt')
fmt = "It's a %A, %B %d, %Y, local time %I:%M:%S%p"
today = time.strftime(fmt, time.localtime())
fout.write(today)
fout.close()
'''



fin = open('today.txt', 'rt')
today_string = fin.read()
#print(today_string)


fmt = "It's a %A, %B %d, %Y, local time %I:%M:%S%p"
#print(datetime.strptime(today_string, fmt))

#print(os.listdir('.'))

#print(os.listdir('..'))


my_birthday = date(1993, 6, 26)
ten_thousands_days = timedelta(days=10000)
print(my_birthday+ten_thousands_days)


print(my_birthday.isoweekday())
















































