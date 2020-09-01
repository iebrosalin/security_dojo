#!/usr/bin/env python

import subprocess
import optparse 
import re
from lib.mac import *

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest = "interface", help = "Interface to change MAC-address")
    parser.add_option("-m", "--mac", dest = "new_mac", help = "New MAC-address")
    (options, arguments) = parser.parse_args()

    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info")
    elif not options.new_mac:
        parser.error("[-] Please specify an MAC-address, use --help for more info")
    return options


options = get_arguments()

interface = options.interface
new_mac = options.new_mac

current_mac = get_current_mac(interface)
print("Current MAC: " + str(current_mac))
change_mac(interface, new_mac)

current_mac = get_current_mac(interface)
if current_mac == options.new_mac:
    print("[+] MAC-address was successfully changed to " + current_mac)
else:
    print("[-] MAC-address did't changed")    