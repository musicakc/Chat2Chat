##Server side of the application

import socket
import sys

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, s.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR) | 1)
host=''
port=2328

print('Socket Created')
try:
    s.bind((socket.gethostname(),port))
except socket.error as e:
    print("Bind has failed. Error: "+str(e[0]))
    sys.exit()

print('Socket Bind Complete')
s.listen(10)
print('Socket now listening')
c,add=s.accept()
print('Connected with '+add[0]+':'+str(add[1]))

while True:
    data=conn.recv(1024)
    print ("Received " + repr(data))
    reply=raw_input('Reply: ')
    c.sendall(reply)

c.close()
