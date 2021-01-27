from Spoofer import Spoofer


class Attacker:
    # for testing in EranKO
    # destinationMac = '14-10-9F-E1-65-61'
    # sourceMAC = '0C-9D-92-82-9F-26'
    # targetIP = '192.168.1.34'
    # gatewayIP = '192.168.1.1' == spoof ip

    def __init__(self, destinationMac='14-10-9F-E1-65-61', sourceMAC='0C-9D-92-82-9F-26', gatewayIP='192.168.1.1', targetIP='192.168.1.34'):
        self.destinationMac = destinationMac
        self.sourceMAC = sourceMAC
        self.gatewayIP = gatewayIP
        self.targetIP = targetIP
        self.s = Spoofer(self.destinationMac, self.sourceMAC, self.gatewayIP, self.targetIP)

    def spoof(self):

        self.s.main()  # this will use spoof and stop_spoof in spoofer

        print("spoofing stopped by attacker")
        self.s.restore(self.targetIP, self.gatewayIP)
        self.s.restore(self.gatewayIP, self.targetIP)

    def main(self):
        pass


a = Attacker()
# a.s.restore("192.168.1.1", "192.168.1.6")
a.spoof()
