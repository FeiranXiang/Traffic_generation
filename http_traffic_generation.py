import http.client as hc
import time

def http_traffic_generation(host = "127.0.0.1", port = 8000, delay = 0, num = 1):
	h = hc.HTTPConnection(host, port)
	while(num):
		num -= 1
		h.request("GET", "/")
		r = h.getresponse()
		print(r.status, r.reason)
		time.sleep(delay)

if __name__ == "__main__":
	http_traffic_generation(delay = 0.2, num = 10)
