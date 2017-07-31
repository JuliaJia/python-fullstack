from socket import *

ADDR = ("127.0.0.1",7500)
ssClient = socket()
ssClient.connect(ADDR)
while True:
    data = input('> ')
    if not data:
        break
    ssClient.send(data.encode())
    data = ssClient.recv(1024).decode()
    if not data:
        break
    print(data)

ssClient.close()
