# import requests
# hit_site = "http://www.google.com"
#
# def hit_site(url):
#     print(url)
#     r = requests.get(url,stream = True)
#     print(r.headers)
#     print(r.encoding)
#     print(r.status_code)
#     print(r.json())
#     print(requests.get(url,stream=True)
#     print(r.request.headers)
#     print(r.response.headers)
#     for line in r.iter_lines():
#         print(line)
#     data = r.text
#     soup = BeautifulSoup(data)
#     return soup

# import pyshark
#
# capture = pyshark.LiveCapture(interface='eth0')
# # capture.sniff(timeout=50)
#
# for packet in capture.sniff_continuously(packet_count=5):
#     print('Just arrived:', packet)
#

# from scapy import *
#
# while 1:
#     sniff(prn=chgSend)
#
# import scapy.all as scapy
# import time
#
# dst_ip = ''
# while 'sniffing':
#     pkt = scapy.sniff(filter=None, count=1)
#     print(pkt[0][1].show())
#
#     pkt[0][1].dst = dst_ip
#     print(pkt[0][1].show())
#
#     break

# scapy.IP()

# targetIP = "1.1.12.1"
# filter_param = "Host" + " " + targetIP
# print(type(filter_param))
# print(filter_param)

