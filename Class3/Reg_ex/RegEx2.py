#print('Hello Class 3')

import re

fname = input('Enter the file name: ')
if len(fname) < 1: fname = 'mbox-short.txt'

fh = open(fname)

ls = list()
print(ls)
print(len(ls))

lnum = 0
for line in fh:
    line = line.rstrip()
    lnum = lnum + 1
    #word = re.findall('[0-9]+', line)
    #wlist = re.findall('[AIEOU]+', line)
    #print(lnum, wlist, word)
    #word = re.findall('^F.+?:', line)
    #print(type(word))
    #if word is not None:
        #print(lnum, word)
    #if re.search('^From: ', line):
    #### to filter the emails ######
    #word = re.findall('^From: (\S+@\S+)', line)

    ##### to extract the domains ##### '^From .*@ ([^ ]*)'
    word = re.findall('^From: (.*\S)', line)
    if len(word) > 0:
        ws = str (word[0])
        print(ws)
        print(type(ws))
        dm = re.findall('@ ([^ ]*)',ws)
        print(lnum, 'Email Id', word, 'Domain', dm)
print(lnum)