
import re

##################### handlig of sample data file #################

#fname = input('Enter the file name: ')
#if len(fname) < 1: fname = 'regex_sum_42.txt'
#
#fh = open(fname)
#
#mylist = list()
##lnum = 0
#sum = 0
##count = 0
#for line in fh:
#    line = line.rstrip()
#    nums = re.findall('[0-9]+', line)
#    #print(nums)
#    if len(nums) > 0:
#        mylist = mylist + nums
##        lnum = lnum + 1
##        print(lnum)
#for i in range(len(mylist)):
#    print(i)
#    sum = sum + int(mylist[i])
#
#print(mylist, sum)

################# handling of actual data file #####################

fname = input('Enter the file name: ')
if len(fname) < 1: fname = 'regex_sum_1757990.txt'

fh = open(fname)

mylist = list()
#lnum = 0
sum = 0
#count = 0
for line in fh:
    line = line.rstrip()
    nums = re.findall('[0-9]+', line)
    #print(nums)
    if len(nums) > 0:
        mylist = mylist + nums
#        lnum = lnum + 1
#        print(lnum)
for i in range(len(mylist)):
    print(i)
    sum = sum + int(mylist[i])

print(mylist, sum)