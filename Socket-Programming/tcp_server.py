from multiprocessing import connection
import socket

host = '127.0.0.1'
port = 12345
BUFFER_SIZE = 1024

# creating tcp type object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_tcp:
    socket_tcp.bind((host, port))

    socket_tcp.listen(5)
    Connection, addr = socket_tcp.accept()

    with Connection:
        print('[*] Established Connection')
        while True:
            data = Connection.recv(BUFFER_SIZE)
            if not data:
                break
            else:
                print('[*] Data Recieved {}' .format(data.decode('utf-8')))
            Connection.send(data)