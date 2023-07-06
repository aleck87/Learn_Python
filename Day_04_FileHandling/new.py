
import pathlib
import os
# current working directory
print(pathlib.Path().absolute())


print('Get current working directory : ', os.getcwd())

apath = os.path.dirname(__file__)
print(apath)
rpath = "read.txt"


fullpath = os.path.join(apath, rpath)
print(fullpath)


fhand = open(r'Letter_To_Father.txt', 'r+')
file = fhand.read()

#file = file.replace('.\n', '.\n\n')
file = file.replace('.', '.\n')
file = file.rstrip()
#print(file)

fhand.write(file)

fhand = open(r'Letter_To_Father.txt', 'r+')
new_file = fhand.read()
#print(new_file)
count = 0
for line in fhand:
    line = line.rstrip()
    if not line.find('Nehru'):
            print('Line No. where Nehru found is:', count, line)

# This Startswith is not working so i need to work with find
#    if line.startswith('Indira'):
#        print('its name: ', line)
print('Line Count:', count)
