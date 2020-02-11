#!/usr/bin/python3

import ipaddress as ip
import platform
import subprocess as sp


def ping(host):
    try:
        output = sp.check_output("ping -{} 1 {}".format('n' if platform.system().lower() == "windows" else 'c', host),
                                 shell=True)
    except:
        return False
    return True


for addr in ip.IPv4Network('192.168.0.0/24'):
    if ping(str(addr)):
        print(addr)
