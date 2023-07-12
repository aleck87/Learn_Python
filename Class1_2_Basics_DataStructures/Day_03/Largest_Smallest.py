largest = 0
smallest = -1
count = 1
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try :
        num_f = int (num)
        if count:
            smallest = num_f
            count = 0
    except :
        print('Invalid input')
        continue
    if num_f > largest :
        largest = num_f

    if num_f <= smallest :
        smallest = num_f


print('Maximun is ', largest)
print('Minimun is ', smallest)