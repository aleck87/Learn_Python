def computepay(h, r):
    if h <= 40 :
        pay =  h * r
    else :
        extra_h = h - 40
        pay =  (40 * r) + (extra_h * (r * 1.5))
    return pay

hrs = input("Enter Hours:")

h = int (hrs)
p = computepay(h, 10.50)
print("Pay", p)