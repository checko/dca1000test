import codecs
import socket
import time

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
DCA1000IP = ('192.168.33.180',4096)
sock.sendto(codecs.decode('5aa50300060001020102031eaaee','hex'),DCA1000IP)
time.sleep(1)
sock.sendto(codecs.decode('5aa509000000aaee','hex'),DCA1000IP)
time.sleep(1)
sock.sendto(codecs.decode('5aa505000000aaee','hex'),DCA1000IP)
