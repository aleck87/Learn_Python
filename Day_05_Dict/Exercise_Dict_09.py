fh = open(r'mbox-short.txt')

maildict = dict()

####### finding email Ids and putting it in a Dict #############
for line in fh:
    if line.startswith('From: '):
        linesp = line.split()
        id = linesp[1]
        maildict[id] = maildict.get(id, 0) + 1

#print(maildict)
######## sorting the most frequent sender ######################
sender = None
bigcount = 0

for key,val in maildict.items():
    if val is None or val > bigcount:
        sender = key
        bigcount = val

print(sender, bigcount)


