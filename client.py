#!/usr/bin/env python
import time
import socket
import struct
s = socket.socket()
s.connect(('127.0.1.1',1234))
string = s.recv(12)
print struct.unpack("iii",string)
while string:
    string = s.recv(8)
    print struct.unpack("ii",string)
    time.sleep(10)
    s.send(struct.pack("ii",9009,0))
