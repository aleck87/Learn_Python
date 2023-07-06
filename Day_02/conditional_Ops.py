abc = 7

if 7 == (70/10):
    print('it worked ')

if abc != (70/100):
    print('it didnt work :(')
else:
    print('ha ha ')

i = 99

if i>100:
    print('galat baat')
else:
    print('Ekdum  sahi')
print(i)

#########################################################################

num = input('give me your DoB:')

try:
    print('Your DoB is: ', int(num))
except:
    print('I expected a number !!!')
# for i