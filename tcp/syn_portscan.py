#!/usr/bin/python3
from scapy.all import *
arr={}
def syn_scan(ip, port):
    pkt = IP(dst=ip)/TCP(dport=port, flags=2)
    result = sr1(pkt, timeout=1, verbose=0)
    if result:
        if result[TCP].flag=='SA':
            print('[+]', port, ' : is open')
            arr[port]='open'
    else:
         print(ip,"port",port,"is close")
         arr[port]='close''  
for i in [20,23,80,139]:
    syn_scan('10.211.55.6', i)
for i in arr:
    print(f'port {i} is {arr[i]}')