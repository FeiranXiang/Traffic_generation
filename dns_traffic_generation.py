from scapy.all import *

def dns_packets():
    a = IP(dst='2.3.4.5',src='5.6.7.8')
    b = UDP()
    c = DNS(id=1,qr=0,opcode=0,tc=0,rd=1,qdcount=1,ancount=0,nscount=0,arcount=0)
    c.qd=DNSQR(qname='www.qq.com',qtype=1,qclass=1)
    p = a/b/c
    send(p)


if __name__ == "__main__":
    dns_packets()
