import socket
import struct

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(("192.168.33.30",5005))

data, addr = sock.recvfrom(1024)
print("%s" % data)
