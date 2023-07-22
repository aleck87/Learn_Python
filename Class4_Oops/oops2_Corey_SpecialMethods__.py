# __repr__ -  The goad of this method is to be unambiguous

# __str__ - The goal of this method is to be readable

import datetime
#import pytz

a = datetime.datetime.utcnow()

b = str(a)

print ('str(a): {}'.format(str(a)))
print ('str(b): {}'.format(str(b)))

print

print ('repr(a): {}'.format(repr(a)))
print ('repr(b): {}'.format(repr(b)))

print

###### Another simple example #####
lst = [1,2,3,4]
stringgg = 'sample string'

print('str(lst): {}'.format(str(lst)))
#print (str(lst))
print (repr(lst))

print (str(stringgg))
#print (repr(stringgg))
print('repr(stringgg): {}'.format(repr(stringgg)))