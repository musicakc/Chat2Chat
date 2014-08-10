##Server.py

import socket
import sys
import time

##Creating a new socket
serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, serversocket.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR) | 1)

host=''
port=2328

print('Socket Created')
try:
    ##Bind the socket to the address
    serversocket.bind((host,port))
except socket.error as e:
    print("Bind has failed. Error: "+str(e[0]))
    sys.exit()

print('Socket Bind Complete')

##Listening for connections made to the socket
serversocket.listen(10)
print('Socket now listening')
##socket.accept() gives two return values where one is a new socket object to send
##and receive messages and the other is the address bound to the socket on the other side
c,add=serversocket.accept()
print('Connected with '+add[0]+':'+str(add[1]))

while True:
    data=conn.recv(1024)
    curTime=time.ctime(time.time())+ "\r\n"
    clientsocket.send(curTime.encode('ascii'))
    print ("Received " + repr(data))
    reply=raw_input('Reply: ')
    c.sendall(reply)
    clientsocket.close()

c.close()
