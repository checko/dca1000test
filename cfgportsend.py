import socket

sockcfg = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
DCA1000IP = ('192.168.33.180',4096)
sockcfg.sendto(b'hello',DCA1000IP)
print("OK")
