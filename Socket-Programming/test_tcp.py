# will get html data of the web

import socket

HOST = input("Enter the web address")
PORT = int(input("Enter port number"))
BUFFERSIZE = 4096
ADDRESS = (HOST,PORT)

if __name__ == '__main__':
    clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSock.connect(ADDRESS)
    while True:
        data = 'GET / HTTP/1.0\r\n\r\n'
        if not data:
            break
        clientSock.send(data.encode('UTF-8'))
        data = clientSock.recv(BUFFERSIZE)
        if not data:
            break
        print(data.decode('UTF-8'))
    clientSock.close()