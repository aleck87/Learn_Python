# This first line is provided for you

hrs = input('Enter Hours:')
h = float(hrs)

rate = input('Enter rate per hour:')
rph = float(rate)

if h <= 40 :
    pay =  h * rph
else :
    extra_h = h - 40
    pay =  (40 * rph) + (extra_h * (rph * 1.5))
print(pay)
