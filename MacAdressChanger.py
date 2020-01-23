#!/usr/bin/env python3

import subprocess as sb
import optparse as opt
import re
import random


def random_mac():
    mac = [0x00, 0x16, 0x3e,
           random.randint(0x00, 0x7f),
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff)]
    return ':'.join(map(lambda x: "%02x" % x, mac))


def get_cmd_arguments():
    parser = opt.OptionParser()
    parser.add_option('-i', '--interface', dest='interface', type='string', help='Specify network interface')
    parser.add_option('-m', '--mac', dest='new_mac', type='string', help='Specify new MAC address')
    (option, arguments) = parser.parse_args()
    if not option.interface:
        parser.error("\n[-] Please specify an interface, use --help for more info.")
    if not (re.match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", str(option.new_mac))):
        option.new_mac = random_mac()
    return option


def change_mac(interface, mac):
    print("[+] Changing MAC address for", interface, "to", mac)
    sb.call(["sudo", "ifconfig", interface, "down"], shell=True)
    sb.call(["sudo", "ifconfig", interface, "hw", "ether", mac], shell=True)
    sb.call(["sudo", "ifconfig", interface, "up"], shell=True)


def get_current_mac(interface):
    ifconfig_result = sb.check_output(["ifconfig", interface]).decode()
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_address_search_result:
        return str(mac_address_search_result.group(0))
    else:
        print("[-] Could not read MAC address")


options = get_cmd_arguments()
old_mac = get_current_mac(options.interface)
new_mac = options.new_mac
change_mac(options.interface, new_mac)

if not old_mac == new_mac:
    print('[+] Old MAC address:', old_mac)
    print('[+] New MAC address:', new_mac)
else:
    print('[-] MAC Address did not get changed')
