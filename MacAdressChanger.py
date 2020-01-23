#!/usr/bin/env python3

import subprocess as sb
import optparse as opt
import re as rx


def get_cmd_arguments():
    parser = opt.OptionParser()
    parser.add_option('-i', '--interface', dest='interface', type='string', help='Specify network interface')
    parser.add_option('-m', '--mac', dest='new_mac', type='string', help='Specify new MAC address')
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("\n[-] Please specify an interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("\n[-] Please specify a MAC address, use --help for more info.")
    return options


def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    sb.check_call(["ifconfig ", interface, " down"])
    sb.check_call(["ifconfig ", interface, " hw ether " + new_mac])
    sb.check_call(["ifconfig ", interface, " up"])


def get_current_mac(interface):
    ifconfig_result = sb.check_output(['ifconfig ', interface])
    mac_address_search_result = rx.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if mac_address_search_result:
        return str(mac_address_search_result.group(0))
    else:
        print("[-] Could not read MAC address")


options = get_cmd_arguments()
old_mac = get_current_mac(options.interface)
# casting
print('[+] Current MAC:' + str(old_mac))
change_mac(options.interface, options.new_mac)
new_mac = get_current_mac(options.interface)
print('[+] Current MAC:' + new_mac)

if old_mac == new_mac:
    print('[+] MAC address successfully changed from', old_mac, ' to ', new_mac)
else:
    print('[-] MAC Address did not get changed')
