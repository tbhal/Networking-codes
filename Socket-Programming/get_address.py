import socket
import sys

try:
    infoList = socket.getaddrinfo(
        'youtube.com', 'www', 0, socket.SOCK_STREAM, 0,
        socket.AI_ADDRCONFIG | socket.AI_V4MAPPED | socket.AI_CANONNAME
    )
except socket.gaierror as e:
    print("Name service failure", e.args[1])
    sys.exit(1)

info = infoList[0]
print(infoList)
socket_args = info[0:3]
address = info[4]
s = socket.socket(*socket_args)
try:
    s.connect(address)
except socket.error as e:
    print('Network failure:', e.args[1])
else:
    print('Success: host', info[3], 'is listening')