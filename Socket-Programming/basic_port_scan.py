import ipaddress
import socket

ip_address = input("Enter IP address or Domain name")

port_init = input("Starting port number: ")
port_end = input("Ending port number: ")

for port in range(int(port_init), int(port_end)):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.timeout(5)
    result = sock.connect_ex((ip_address, port))
    if result == 0:
        print(port, "--> Open")
    else:
        print(port, "--> Closed")
    sock.close()