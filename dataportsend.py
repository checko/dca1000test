import socket

sockdata = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
PCIP = ('192.168.33.30',4098)
sockdata.sendto(b'Hello !',PCIP)
print("OK")
