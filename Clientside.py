#!/usr/bin/python           

import socket               

s = socket.socket()         
host = socket.gethostname() 
port = 8000              

s.connect((host, port))
print(s.recv(1024))
t = input("Inter a message to send over server: ")
s.sendall(t.encode())
s.close                  

