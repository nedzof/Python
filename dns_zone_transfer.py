#!/usr/bin/python3
# for server in $(host -t ns nedzo.ch | grep "name server" | cut -d " " -f4);do host -l nedzo.ch $server;done93.188.73.211

import optparse as opt
import subprocess as sb


def get_cmd_arguments():
    parser = opt.OptionParser()
    parser.add_option('-h', '--host', dest='host', type='string', help='Specify host')
    (option, arguments) = parser.parse_args()
    if not option.host:
        parser.error("\n[-] Please specify a host, use --help for more info.")
    else:
        return option


options = get_cmd_arguments()
host = options.host
sb.call(["for server in $(host -t ns ", host, " | grep "'name server'" | cut -d " " -f4);do host -l ", host,
         " $server;done"], shell=True)
