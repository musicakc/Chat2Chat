##Client side of application

import socket
import sys
import time

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host=''
port=2323

print("Socket Created")
s.connect(('localhost',port))
print s.recv(1024)
while True:
        message=raw_input('Enter message: ')
        s.send(message)
        print("Waiting for reply")
        reply=s.recv(1024)
        print('Received: ',repr(reply))

print "The time is" + reply.decode('ascii')
s.close()
