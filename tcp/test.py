# 单个IP全端口扫描
import time  
import socket  
import threading 
from scapy.all import *
  

class SingelIP_Scan:
    def connScan(self, tgtHost, tgtPort, name):  
        try:  
            # SYN扫描
            syn = IP(dst=tgtHost)/TCP(dport=tgtPort, flags=2)
            result_raw = sr(syn, iface='enp6s0f0', timeout=1, verbose=False)  # Linux下少了iface参数，需要加上
            result_list = result_raw[0].res
            for i in range(len(result_list)):
                if result_list[i][1].haslayer(TCP):
                    TCP_fields = result_list[i][1].getlayer(TCP).fields
                    if TCP_fields['flags'] == 18:
                        port = TCP_fields['sport']
                        # print('[+]', port, ' : is open', name)
                        n = News(tgtHost, port, name)
                        n.insert()
                        logger.warning('from: ' + name +  ' insert [+] ' + tgtHost + ' [+] ' + str(port) + ' : is open')

        except:   
            # print("[-]%d/tcp close" % tgtPort)  
            pass
      
    def portScan(self, tgtHost, name):  
        try:  
            tgtIP = socket.gethostbyname(tgtHost)  
        except:  
            # print("[-]cannot connect %s" % tgtIP)  
            logger.warning(' [-] ' + tgtIP + ' can not connect')
            return  

        # print("\n[+]scan results for:" + tgtIP)   
        if '_' in name:
            result = name.split('_')
            name = result[0]
            if result[1].isdigit():
                port = int(result[1])
                self.connScan(tgtHost, port, name)
            else:
                for port in range(0, 65535):  
                    time.sleep(1)
                    print("scanning port:" + str(port)) 
                    t2 = threading.Thread(target=self.connScan, args=(tgtHost, port, name))
                    # t.daemon = True
                    t2.start() 
                    # self.connScan(tgtHost,int(port), name)   
        else:
            for port in range(0, 65535):  
                time.sleep(1)
                # print("scanning port:" + str(port))  
                t3 = threading.Thread(target=self.connScan, args=(tgtHost, port, name))
                # t.daemon = True
                t3.start()

