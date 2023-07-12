fname = input("Enter file name: ")

try:
    fh = open(fname)
except:
    print('File can not be opened: ', fname)
    quit()

count = 0
collect = 0.0
for line in fh:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    print(line)
    count = count + 1
    fval_s = line[20:]
    print(fval_s)
    fval_f = float(fval_s)
    print(fval_f)
    print(type(fval_f))
    collect = collect + fval_f

print('Total F val count is: ', fval_f)
print('Number of F val is: ', count)
avg = collect/count
print('Average spam confidence:', avg)
