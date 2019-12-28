import socket
import re
import time
import threading
import progressbar

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
        pass
ip = input('введите ip:\n')
start_time = time.time()
bar = progressbar.ProgressBar(maxval=10.0).start()

t = 0
while t<= 1.0:
    bar.update(t)
    time.sleep(0.01)
    t+=0.01
for i in range(10000):
    scan_port(ip,i)
    if (i == 0):
        print('не имеется открытых портов')
time.sleep(0.1)
bar.finish()
TimeOfProgram = (time.time() - start_time)
print (toFixed((TimeOfProgram),2),'second')
