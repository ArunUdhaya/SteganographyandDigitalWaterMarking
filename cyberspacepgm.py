import socket
import pcapy
from struct import *

# set the network interface and filter
dev = "eth0"
filter = "tcp"

# open the network interface for capture
cap = pcapy.open_live(dev, 65536, 1, 0)

# set the filter
cap.setfilter(filter)

# process packets in a loop
while True:
    try:
        # read a packet from the network interface
        (header, packet) = cap.next()

        # extract the IP header from the packet
        ip_header = packet[0:20]
        iph = unpack('!BBHHHBBH4s4s', ip_header)

        # extract the TCP header from the packet
        tcp_header = packet[iph[0] * 4:iph[0] * 4 + 20]
        tcph = unpack('!HHLLBBHHH', tcp_header)

        # get the source and destination IP addresses and ports
        source_ip = socket.inet_ntoa(iph[8])
        dest_ip = socket.inet_ntoa(iph[9])
        source_port = tcph[0]
        dest_port = tcph[1]

        # check if the packet is an HTTP request
        if dest_port == 80:
            data = packet[iph[0] * 4 + tcph[4] * 4:]
            if b"POST" in data:
                print("[+] Possible digital theft detected!")
                print(f"    Source IP: {source_ip}")
                print(f"    Source port: {source_port}")
                print(f"    Destination IP: {dest_ip}")
                print(f"    Destination port: {dest_port}")
                print(f"    Data: {data}")

    except KeyboardInterrupt:
        break