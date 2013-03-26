#!/usr/bin/env python
import time
import socket
import struct
s = socket.socket()
s.connect(('127.0.1.1',1234))
string = s.recv(12)
print struct.unpack("iii",string)
while string:
    s.send(struct.pack("ii",4004,0))
    string = s.recv(12)
    print struct.unpack("iii",string)
    time.sleep(10)
