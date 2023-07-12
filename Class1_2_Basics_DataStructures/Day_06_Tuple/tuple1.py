filename = input('Enter the File Name: ')
if len(filename) < 1 : filename = 'mbox-short.txt'

fh = open(filename)
dt = dict()
for item in fh:
    if item.startswith('From '):
        stsplit = item.split()
#        print(stsplit)
        str_time = stsplit[5]
#        print(str_time)
        hour = str_time[:2]
#        print(type(hour))
#        print(hour)
        dt[hour] = dt.get(hour, 0) + 1

sl = sorted(dt.items())
print(sl)

################ print sliced list ################
print(sl[:5])

for k,v in sorted(dt.items()):
    print(k,v)


#tups = sorted(dt.items())
#for i in range(len(tups)):
#    print(tups[i])


#print(type(tups))
#print(tups)
#dts = sorted(dt.items())
#for i in dts:
#    print(i)