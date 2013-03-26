#!/usr/bin/env python
import time
import socket
import struct
s = socket.socket()
s.connect(('127.0.1.1',1234))
string = s.recv(20)
print struct.unpack("qqi",string)
while string:
<<<<<<< HEAD
    s.send(struct.pack("qqi",*struct.unpack("qqi",string)))
    string = s.recv(20)
    print struct.unpack("qqi",string)
    time.sleep(5)
=======
    s.send(struct.pack("ii",4004,0))
    string = s.recv(12)
    print struct.unpack("iii",string)
    time.sleep(10)
>>>>>>> 57d31e8... modify client.py
