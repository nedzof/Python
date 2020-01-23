#!/usr/bin/env python3

import subprocess as sb
import optparse as opt
import re as rx
import random

def randomMAC():
    return 1

def get_cmd_arguments():
    parser = opt.OptionParser()
    parser.add_option('-i', '--interface', dest='interface', type='string', help='Specify network interface')
    parser.add_option('-m', '--mac', dest='new_mac', type='string', help='Specify new MAC address')
    (option, arguments) = parser.parse_args()
    if not option.interface:
        parser.error("\n[-] Please specify an interface, use --help for more info.")
    elif not option.new_mac:
        parser.error("\n[-] Please specify a MAC address, use --help for more info.")
    return option


def change_mac(interface, mac):
    print("[+] Changing MAC address for", interface, "to", mac)
    sb.call(["ifconfig", interface, "down"], shell=True)
    sb.call(["ifconfig " + interface + " hw ether " + mac], shell=True)
    sb.call(["ifconfig", interface, "up"], shell=True)


def get_current_mac(interface):
    ifconfig_result = sb.check_output(["ifconfig", interface]).decode()
    mac_address_search_result = rx.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_address_search_result:
        return str(mac_address_search_result.group(0))
    else:
        print("[-] Could not read MAC address")


options = get_cmd_arguments()
old_mac = get_current_mac(options.interface)
# casting
print('[+] Old MAC:' + old_mac)
change_mac(options.interface, options.new_mac)
new_mac = get_current_mac(options.interface)
print('[+] New MAC:' + new_mac)

if old_mac == new_mac:
    print('[+] MAC address successfully changed from', old_mac, 'to', new_mac)
else:
    print('[-] MAC Address did not get changed')
