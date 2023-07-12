print('This is the chapter file handling')

#fhand = open('Letter_To_Father.txt')
#fhand = open('thes.txt')
#inp = fhand.read()
#
#print('No. of lines in file', len(inp))
##print(lines)
#print('Type of fhand' , type(fhand))
#print('Type of inp' , type(inp))

Thes = 0

# This is for printing the whole file: read a file in an string and then  print it
#print(inp)
fhand = open('read.txt', "r")
inp = fhand.read()
for line in fhand:
    print(line)
#    #if line.startswith('The ', [0 , 89]):
#    if line.find('The'):
#        print(line)
#        Thes = Thes + 1
#        print('No of The', Thes)