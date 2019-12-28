import socket
import re
import time
import threading

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"
def scan_port(ip,port):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.settimeout(0.5)
    try:
        connect = sock.connect((ip,port))
        print("Port:",port,"it's open")
        connect.close()
    except:
        #print('не имеется открытых портов')
        pass
a = input()
b = input()
c = input()
d = input()

ip = (str(a)+'.'+str(b)+'.'+str(c)+'.'+str(d))
start_time = time.time()
for i in range(10000):
    scan_port(ip,i)
    if (i == 0):
        print('не имеется открытых портов')
TimeOfProgram = (time.time() - start_time)
print (toFixed((TimeOfProgram),2),'second')
