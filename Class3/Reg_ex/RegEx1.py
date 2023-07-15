#print('Hello Class 3')

import re

fname = input('Enter the file name: ')
if len(fname) < 1: fname = 'mbox-short.txt'

fh = open(fname)

for line in fh:
    line = line.rstrip()
    #if re.search('^From: ', line):
    #if re.search('^From: ([@])', line):
    #if re.search ('(^X.*)', line):
    #if re.search ('(^X.*?)', line):
    if re.search ('(^X-\S+:)', line):
    #if re.search('From: ', line):
    #if re.search('umich (ID*?)', line): #doesnt work
        print(line)

#print(find)

lin = From louis@media.berkeley.edu Fri Jan  4 18:10:48 2008
y = re.findall('@ ([^ ]*)', lin)
print(y)