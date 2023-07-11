
############# Lists of Numbers and handling ###############

# fl = [2,34,6,78,57,88,435,38658,35,242,234,65354,6]
#
# print(type(fl))
#

#
# for i in range(len(fl)):
#
#     if fl[i] > 1000:
#
#         print('Greater than 1000 is: ', fl[i] , '\nfound at position: ', i )

# average = sum(fl)/len(fl)
#print('Avarage is :', average)

## above works for looping in List #####

###########creating a structure type in list #######################

        #emp id     #name dob               # nick name
#name = input('Enter the name: ')
#fl2  = [1314434, ['Deepak', 'DoB- 10/10/1987'], 'Nick Name: Bablu',
#        1314477, ['Sudhir', 'DoB- 10/10/1987'], 'Nick Name: Bachcha',
#        1314456, ['Ali', 'DoB- 10/10/1987'], 'Nick Name: Ali the Power',
#        1317678, ['Atul', 'DoB- 10/10/1987'], 'Nick Name: Budhauu']

#### Split of string into List #####
str = 'Hi there, I am learning Python'

l_split = str.split()
print(l_split)

for i in range(len(l_split)):
    if 'Python' in l_split[i]:
        print(l_split[i])

############# Collection of Emails from a file: mbox-short.txt ###########
file = input('Enter the File name: ')
if len(file) < 1 : file = 'mbox-short.txt'

fh = open(file)
# fl = fh.read()

email_list = list()
count = 0
for line in fh:
    if line.startswith('From '):
        temp_list = line.split()
        email_list.append(temp_list[1])
        count= count + 1

for j in range(len(email_list)):
    print(email_list[j])
print('There were', count, 'lines in the file with From as the first word ')