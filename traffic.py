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

import scapy.all as scapy

pkt = scapy.sniff(count=2)

print(pkt)

