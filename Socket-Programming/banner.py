import socket
import re

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

web = input(' Enter website')
sock.connect((web, 80))

httpGet = b"Get / HTTP/1.1\nHost: web\n\n"
data = ''
try:
    sock.sendall(httpGet)
    data = sock.recvfrom(1024)
    strdata = data[0]
    headers = strdata.splitlines()
    for header in headers:
        print(header.decode())

except socket.error:
    print("Socket error", socket.error)
finally:
    print('Closing connection')
    sock.close()