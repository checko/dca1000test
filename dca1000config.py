import codecs
import socket
import time
import struct
import numpy as np

sockcfg = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
DCA1000IP = ('192.168.33.180',4096)

sockdata = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
PCIP = ('192.168.33.30',4098)
sockdata.bind(PCIP)

sockdata.settimeout(10)

# start recording
sockcfg.sendto(codecs.decode('5aa50300060001020102031eaaee','hex'),DCA1000IP)
time.sleep(1)
sockcfg.sendto(codecs.decode('5aa509000000aaee','hex'),DCA1000IP)
