score = input('Enter score:')
scr = float(score)

if((scr <= 1.0) and (scr>=0.0)) :
    if ((scr <= 1.0) and (scr>=0.9)) :
        print('A')
    elif ((scr < 0.9) and (scr>=0.8)) :
        print('B')
    elif ((scr < 0.8) and (scr>=0.7)) :
        print('C')
    elif ((scr < 0.7) and (scr>=0.6)) :
        print('D')
    else :
        print('F')
else:
    print('Range is between 0.0 to 1.0')