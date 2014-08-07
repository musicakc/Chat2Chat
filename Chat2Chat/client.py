##Client side of application

import socket
import sys

host='32.213.14.5'
port=2323

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Socket Created")
s.connect((host,port))
print s.recv(1024)
while True:
        message=raw_input('Enter message: ')
        s.send(message)
        print("Waiting for reply")
        reply=s.recv(1024)
        print('Received: ',repr(reply))
s.close()
