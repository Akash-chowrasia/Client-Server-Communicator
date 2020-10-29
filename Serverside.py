#!/usr/bin/python           
import socket               

s = socket.socket()         
host = socket.gethostname() 
port = 8000                
s.bind((host, port))       
s.listen(5)                
while True:
   clientside, address = s.accept()    
   print('connected stablished with client at: ', address)
   t = "connection message sent from server"
   clientside.send(t.encode())
   print(clientside.recv(1024))
   clientside.close()               
