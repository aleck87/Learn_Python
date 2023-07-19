#import urllib.request, urllib.parse, urllib.error


#fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
#fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
#fhand = urllib.request.urlopen('http://data.pr4e.org/')  #### for whole web page, which can ne downlaoded to a string
#for line in fhand:
#    #print(line.decode())
#   print(line.decode().strip())

#############################################################################

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
print(type(fhand))

counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)
