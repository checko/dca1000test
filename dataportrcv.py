import socket

sockdata = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
PCIP = ('192.168.33.30',4098)

sockdata.bind(PCIP)

data, addr = sockdata.recvfrom(1024)
print(data)
