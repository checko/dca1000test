import socket
import codecs

DCA1000EVMIP = ('192.168.33.180',4096)

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.sendto(codecs.decode('5aa506000000aaee','hex'),DCA1000EVMIP)
