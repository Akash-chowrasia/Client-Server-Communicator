
'''
    This module is to be executed at client side
    to communicate with server.
'''
#from serverside import PORT
from time import sleep
import socket

def connect_with_server():
    '''
        This function sends request to the server for connection.
    '''
    s.connect((host, PORT))
    sleep(2)
    print("Connection request sent...")

def message_parser():
    '''
      This function treams and extracts the message from the returned
      encoded output by server.
    '''
    return str(message)[2:-1]

def input_message():
    '''
      This function ask's Client operator to responce
      for senting to the Server.
    '''
    return input("Enter Responce: ")

def send_message_to_server():
    '''
      This function sends message towards the respective client.
    '''
    s.sendall(message.encode())

# Driver Code
if __name__ == "__main__":
    s = socket.socket()
    host = socket.gethostname()
    PORT = 8000
    connect_with_server()
    message = s.recv(1024)
    print("connection established..")
    sleep(1)
    print("Message from Server: ",message_parser())
    sleep(2)
    message = input_message()
    send_message_to_server()
    print("Message sent successfully...")
    sleep(1)
    s.close()
    print("Connection closed...")
