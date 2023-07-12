
v1 = input('enter the first value:')
type(v1)
v2 = input('enter the 2nd value:')

val1 = int (v1)
val2 = int(v2)
print ('this is the typ eof v2', type(v2))

def addition(val1, val2):
    print('the parameters are', val1, val2)
    res =  val1 +  val2

    print('the result of addition is', res)
    return res

addition(val1, val2)