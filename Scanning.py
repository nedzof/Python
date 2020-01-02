import socket
import os
import sys
import ipaddress



def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except:
        return


def checkVulns(banner):
    if 'FreeFloat Ftp Server (Version 1.00)' in banner:
        print('[+] FreeFloat FTP Server is vulnerable.')
    elif '3Com 3CDaemon FTP Server Version 2.0' in banner:
        print('[+] 3CDaemon FTP Server is vulnerable.')
    elif 'Ability Server 2.34' in banner:
        print('[+] Ability FTP Server is vulnerable.')
    elif 'Sami FTP Server 2.0.2' in banner:
        print('[+] Sami FTP Server is vulnerable.')
    else:
        print('[-] FTP Server is not vulnerable.')
        return


def main():
    """ips = ['192.168.95.148', '192.168.95.149']"""
    ports = [21, 80, 443]
    """for num, x in enumerate(ips, start=1):"""
    for ip in ipaddress.IPv4Network('192.168.1.0/24'):
        """for i in range(256):"""
        """ip = "192.168.0.%d" % (i)"""
        for port in ports:
            banner = retBanner(ip, port)
        if banner:
            print('[+] ' + banner + ': ' + ip + ':' + port)
        else:
            print('Banner:{}, {}:{} failed'.format(banner, ip, port))


if __name__ == '__main__':
    main()
