fname = input(' Give the file name: ')
Search_word = input('Give the word you want to search in file: ')
try:
    fhand = open( fname, 'r+')
except:
    print('file can not be opened:', fname)
    quit()
numofoccureance = 0
for count in fhand:
    count = count.rstrip()
    if Search_word in count:
        numofoccureance = numofoccureance + 1
        print(count)
print('Your word', Search_word, 'appeared ',numofoccureance, 'Times')
