from scapy.all import sniff, IP

def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        print(f"[+] Packet: {ip_src} -> {ip_dst}")
        print(f"[*] Summary: {packet.summary()}")

def main():
    print("Starting network sniffer...")
    sniff(prn=packet_callback, store=0)

if __name__ == "__main__":
    main()

from scapy.all import sniff, IP, TCP, UDP

def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        proto = packet[IP].proto
        print(f"[+] Packet: {ip_src} -> {ip_dst} (Proto: {proto})")

        if TCP in packet:
            tcp_sport = packet[TCP].sport
            tcp_dport = packet[TCP].dport
            print(f"[*] TCP Packet: {ip_src}:{tcp_sport} -> {ip_dst}:{tcp_dport}")

        elif UDP in packet:
            udp_sport = packet[UDP].sport
            udp_dport = packet[UDP].dport
            print(f"[*] UDP Packet: {ip_src}:{udp_sport} -> {ip_dst}:{udp_dport}")

        print(f"[*] Summary: {packet.summary()}")

from scapy.all import sniff, IP, TCP
from scapy.layers.http import HTTPRequest

def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        print(f"[+] Packet: {ip_src} -> {ip_dst}")

        if packet.haslayer(HTTPRequest):
            http_layer = packet.getlayer(HTTPRequest)
            print(f"[*] HTTP Request: {http_layer.Method.decode()} {http_layer.Host.decode()}{http_layer.Path.decode()}")

        print(f"[*] Summary: {packet.summary()}")
