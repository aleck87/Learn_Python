################ simple things with Dict #############
#purse = dict()
#
#purse['money'] = 12
#purse['tissue'] = 120
#purse['coins'] = 10
#
#print(purse)
#print(purse['tissue'])
#purse['tissue'] = purse['tissue'] + 20
#print(purse['tissue'])

########### Histogram of words #####################
#myDict = dict()

#fh = open(r'LetterToFather.txt', '+r')
#
#for line in fh:
#    mywordlist = line.split()
#    for word in mywordlist:
#        if word not in myDict:
#            myDict[word] = 1
#        else:
#            myDict[word] = myDict[word] + 1
#print(myDict)

########### Histogram of words improved with method "get" #####################

myDict = dict()

fh = open(r'LetterToFather.txt', '+r')

for line in fh:
    mywordlist = line.split()
    for word in mywordlist:
        myDict[word] = myDict.get(word, 0) + 1
#        val = myDict.values()
#        print(val)

#for key in myDict:
#    print(key, myDict[key])
#print(myDict)
bigword = None
bigcount = 0

for k,v in myDict.items():
    if v is None or v > bigcount:
        bigword = k
        bigcount = v
print(bigword, bigcount)