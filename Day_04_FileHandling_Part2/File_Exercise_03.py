
############## Assignment 8.4 #######################
#
#file = input('Enter the File name: ')
#
#fh = open(file)
#fl = fh.read()
#l_file = fl.split()
#
#new_list = list()
#
#for i in range(len(l_file)):
#    if i==1: new_list.append(l_file[i])
#    elif not l_file[i] in new_list: new_list.append(l_file[i])
#
#new_list.sort()
#print(new_list)

############## Assignment 8.5 #######################
#file = input('Enter the File name: ')
#
#fh = open(file)
## fl = fh.read()
#
#email_list = list()
#count = 0
#for line in fh:
#    if line.startswith('From '):
#        temp_list = line.split()
#        email_list.append(temp_list[1])
#        count= count + 1
#
#for j in range(len(email_list)):
#    print(email_list[j])
#print('There were', count, 'lines in the file with From as the first word ')

############## Assignment 8.5 improvement #######################

file = open('mbox-short.txt')
count = 0
for line in file:
    line = line.rstrip()
    words = line.split()
    if words[1:2] != 'From: ' :
        print(words[1:2])
        continue
    count=+ count
    print(words[2])

print('There were', count, 'lines in the file with From as the first word ')
