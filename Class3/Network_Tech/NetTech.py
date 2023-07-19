import socket
# cratng myscoket with some magic - i dont understand atm
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.getaddrinfo('localhost', 8080)
# connect to the URL /Web or Web Server , PORT
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
#cmd = 'GET http://bosch.com/* HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()

##### end with error ####
#  File "C:\D\04_Work_Learn\Learn_Python\Class3\Network_Tech\NetTech.py", line 5, in <module>
#    mysock.connect(('data.pr4e.org', 80))
#socket.gaierror: [Errno 11001] getaddrinfo failed