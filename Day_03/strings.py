print('hello string')

str1 = 'Deepak Kumar Varma'
str2 = 'learing Python'

str3 = str1 + str2

for i in str3 :
   # print(str3[i]) this doesnt work because i here is the actual value in the cell of str3
   #print(i)
   if i == 'D' :
      print('thats the start of Name')
print('length', len(str3))

# string slicing, the last entry as here 6 in not included
print(str3[0:6])

# remember python goes beyond the length of str but it dosnt print or access beyond it
print(str3[6:55])

str_num = '133456 '

print('conversion of a string of number to actual number', int(str_num), type(str_num))
print(int(str_num) + 7)

print( 'bla',str_num*2)