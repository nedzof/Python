#!/usr/bin/env python3

"""
ifconfig eth0 down
ifconfig eth0 hw ether 00:11:22:33:44:55 // 12 Characters
ifconfig eth0 up
ifconfig eth0
"""

import subprocess as sb
import optparse as opt


def get_arguments():
    parser = opt.OptionParser()
    parser.add_option('-i', '--interface', dest='interface', type='string', help='Specify network interface')
    parser.add_option('-m', '--mac', dest='new_mac', type='string', help='Specify new MAC address')
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
        exit(0)
    elif options.new_mac:
        parser.error("[-] Please specify a MAC address, use --help for more info.")
        exit(0)
    return options


def change_mac(iface, mac):
    print("[+] Changing MAC address for " + iface + " to " + mac)
    sb.check_call(["ifconfig ", iface, " down"], shell=True)
    sb.check_call(["ifconfig ", iface, " hw ether " + mac], shell=True)
    sb.check_call(["ifconfig ", iface, " up"], shell=True)
    sb.check_call(["ifconfig ", iface], shell=True)


change_mac(options.interface, options.new_mac)
