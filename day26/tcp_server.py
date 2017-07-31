from socket import *
from time import ctime
ADDR = ("127.0.0.1",7500)
ss = socket()
ss.bind(ADDR)
ss.listen(5)
while True:
    print("waiting for connection...")
    ssClient, addr = ss.accept()
    print("...connected from :",addr)
    while True:
        data = ssClient.recv(1024).decode()
        if not data:
            break
        ssClient.send(('[%s] %s' % (ctime(),data)).encode())

    ssClient.close()

ss.close()