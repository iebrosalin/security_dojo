#!/usr/bin/env python

import optparse 
import scapy.all as scapys

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-t","--target", dest = "target", help = "Target IP / IP range.")
    (options, arguments) = parser.parse_args()
    return options

def scan(ip):
    arp_request = scapys.ARP(pdst = ip)
    broadcast = scapys.Ether(dst = "ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapys.srp(arp_request_broadcast, timeout = 1, verbose = False)[0]

    client_list = []

    for element in answered_list:
        client_dict = {"ip":element[1].psrc, "mac": element[1].hwsrc}
        client_list.append(client_dict)
    return client_list

def print_result(results_list):
    print("IP\t\tMAC-address\n----------------------------------")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])

target_ip = get_arguments().target
scan_result = scan(target_ip)
print_result(scan_result)
