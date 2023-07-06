Days = ['Mon', 'Tues', 'weds', 'thurs']
Days.append('Friday')

for day in Days:
    print(day)
file = input('Enter the filename: ')
fh = open(file, '+r')

romeo = fh.read()
#print(romeo)
NumOfLines = 0
for line in fh:
    #line = line.rstrip()
    print(line)
    #NumOfLines = NumOfLines + 1

print(NumOfLines)

