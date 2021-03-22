import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--ip", dest = "ip", help = "IP target")
    parser.add_option("-p", "--port", dest = "port", help = "Port target")
    (options, arguments) = parser.parse_args()

    return options