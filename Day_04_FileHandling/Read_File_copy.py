###
#
#
from pathlib import Path
print(Path.cwd())

print('This is the chapter file handling')

#fhand = open("C:\D\04_Work_Learn\Learn_Python\Day_04_FileHandling\read.txt")
fhand = open("./read.txt")
inp = fhand.read()
print(inp)
count = 0
for line in fhand:
    if line.startswith('The '):
        print(line)

    print(count)
