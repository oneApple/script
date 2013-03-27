#!/usr/bin/env python
import time
import socket
import struct
s = socket.socket()
s.connect(('127.0.1.1',1234))
string = s.recv(20)
print struct.unpack("qqi",string)
while string:
    s.send(struct.pack("qqi",*struct.unpack("qqi",string)))
    string = s.recv(20)
    print struct.unpack("qqi",string)
    time.sleep(5)
