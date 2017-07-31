from socket import *

ADDR = ("127.0.0.1",7000)
ssClient = socket()
ssClient.connect(ADDR)
while True:
    data = input('> ')
    if not data:
        break
    ssClient.send(data)
    data = ssClient.recv(1024)
    if not data:
        break
    print(data.decode('uft-8'))

ssClient.close()
