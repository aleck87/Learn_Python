print('Hello Tuple')

tu = ('me', 'mine', 'only me')  # tuples are im-mutable

print(tu[0]) #print with index

for i in tu: # loop through the element - not index like in list
    print(i)

print(max(tu)) #functions works with tuple like list but tuples are immutable

try:
    tu.__add__(you)
except:
    print('tuples are immutable')

mytup = 'Deepak', 'Anahita', 'python'

me, mine , onlyme = 'Deepak', 'Anahita', 'Free'
print(me)
print(tu)

# when traversing through a Dict, it returns a tuple
d = dict()
d['me'] = 'Deepak'
d['Mine'] = 'Anahita'

for (k,v) in d.items():
    print(k,v)

#assign the items from dict to tuple
tups = d.items()
print(tups)

if tu > mytup:
    print('this is tuple tu', tu)
    print('this is tuple mytup', mytup)
    print('This is the comparison between tuples and it works in int, str and ..')

#sort the tuple
sorted(mytup)
print('sorted mytup in string items dosnt work', mytup)

numtup = 4,57,8,8685,99
sorted(numtup)
print(('sorting in int tuple', numtup))

# sorting in tuple doesnt work caz they are immutable

################## BUT tuples in a Dict are sortable due to there support of comparison functionality
D_num = {'a':2,'c':0, 'b':35465, 'f':562}
print('Normal Dict: ', D_num)
print('sorted dict ',sorted(D_num.items()))
tus = sorted(D_num.items()) # assign the sorted dict items into a tuple and then use them as you want
#print('sorted dict assigned to tuple', tus)

sorted_Dict = dict()
sorted_Dict = sorted(D_num.items())
print(' sorted dict assign to another dict', sorted_Dict)

################ Lists: have a unique Keys but values can be same ##########
# So sorting based on values are tricky: lets see
temp_l = list()
for k,v in D_num.items():
    temp_l.append((v,k))
print(temp_l)

#sort this list
temp_l = sorted(temp_l, reverse=True)
print('Sorted list: ', temp_l)

temp_l.sort()