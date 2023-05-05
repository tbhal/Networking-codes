# naive client-server chat

import socket, sys

UDP_IP = '127.0.0.1'
UDP_PORT = 12345
BUFFER = 4096

socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

socket_server.bind((UDP_IP,UDP_PORT))

while True:
    print("Waiting for client ............")
    data, address = socket_server.recvfrom(BUFFER)
    data = data.strip()
    print("Data Recieved from address: ", address)
    print("message: ",data)

    try:
        respons = "ohio %s" % sys.platform()
    except Exception as e:
        respons = "%s" % sys.exc_info()[0]
    print("Response", respons)

    socket_server.sendto(respons.encode(), address)
    socket_server.close()