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
time.sleep(1)
sockcfg.sendto(codecs.decode('5aa505000000aaee','hex'),DCA1000IP)
pp=0;
packet_num = []
byte_count = []
for i in range(100):
    data, addr = sockdata.recvfrom(4096)
    packet_num.append(struct.unpack('<1l', data[:4])[0])
    byte_count.append(struct.unpack('>Q', b'\x00\x00' + data[4:10][::-1])[0])
    packet_data = np.frombuffer(data[10:], dtype=np.uint16)
 #   print(packet_num, byte_count,byte_count-pp)
 #   pp=byte_count

for i in range(len(byte_count)):
    if(i==0):
        print(packet_num[i],byte_count[i])
    else:
        print(packet_num[i],byte_count[i],byte_count[i]-byte_count[i-1])


#stop recording
sockcfg.sendto(codecs.decode('5aa506000000aaee','hex'),DCA1000IP)
