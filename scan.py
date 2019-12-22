import socket
import re

def scan_port(ip,port):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.settimeout(0.5)
    try:
        connect = sock.connect((ip,port))
        print("Port:",port,"it's open")
        connect.close()
    except:
        pass
a = input()
b = input()
c = input()
d = input()
ip = (str(a)+'.'+str(b)+'.'+str(c)+'.'+str(d))
for i in range(1000):
    scan_port(ip,i)
