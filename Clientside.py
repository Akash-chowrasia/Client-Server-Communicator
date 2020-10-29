#!/usr/bin/python           

import socket               

s = socket.socket()         
host = socket.gethostname() 
port = 8000              

s.connect((host, port))
print(s.recv(1024))
t = "Thanks from Client!!!"
s.sendall(t.encode())
s.close                  

