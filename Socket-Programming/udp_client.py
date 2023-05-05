from cgitb import reset
from email import message
import socket

UDP_IP = '127.0.0.1'
UDP_PORT = 12345
BUFFER = 4096

address = (UDP_IP, UDP_PORT)

socket_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    Message = input('Enter your message > ')
    if Message == 'exit':
        break
    socket_client.sendto(Message.encode(), address)
    responce, addr = socket_client.recvfrom(BUFFER)
    print("Server response +> %s" % responce)
    
socket_client.close()