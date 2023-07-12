fname = input("Enter file name: ")

try:
    fh = open(fname)
except:
    print('File can not be opened: ', fname)
    quit()


file_content = fh.read()
newfile = file_content.upper()
print(newfile.rstrip())

#for line in fh:
#    line = line.rstrip()
#    print(line)