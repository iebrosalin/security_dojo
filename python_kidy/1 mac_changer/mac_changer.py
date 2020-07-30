#!/usr/bin/env python

import subprocess
import optparse
import re

def get_arguments():
    parser = optparser.OptionParser()
    parser.add_option("-i", "--interface", dest = "interface", help = "Interface to change MAC-address")
    parser.add_option("-m", "--mac", dest = "new_mac", help = "New MAC-address")
    (options, arguments) = parser.parse_args()
    if not option.inteface
        parse.error("[-] Please specify an interface, use --help for more info")
    elif not option.new_mac
                parse.error("[-] Please specify an MAC-address, use --help for more info")
    return options

def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw ether" + new_mac])
    subprocess.call("ifconfig", interface, "up"])
    
def get_current_mac(interface):
    ifocnfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if(mac_address_search_result):
        return mac_address_search_result.group(0)
    else:
        print("[-] Sorry MAC-address not found")


(options, arguments) = get_arguments()

# interface = input("interface > ") # raw_input for python 2.7
# new_mac = input("new MAC > ")

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