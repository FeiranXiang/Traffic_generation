import http.client as hc
import time
from multiprocessing import Pool
import os, time, random
from SYNflood import synFlood

def http_traffic_generation(host = "127.0.0.1", port = 8000, delay = 0, num = 1):
	h = hc.HTTPConnection(host, port)
	while(True):
		num -= 1
		h.request("GET", "/")
		r = h.getresponse()
		print(r.status, r.reason)
		#time.sleep(delay)

if __name__ == "__main__":
	p = Pool(16)
	for i in range(16):
		p.apply_async(synFlood)
	p.close()
	p.join()	
	#http_traffic_generation(delay = 0.2, num = 10)
