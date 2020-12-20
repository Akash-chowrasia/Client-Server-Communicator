'''
    This module is to be executed at Server side
    to communicate with Clients.
'''
import socket
from time import sleep

def client_listener():
    '''
      This function looks for cient for connection.
    '''
    clientside, address =  s.accept()
    return [clientside, address]

def input_message():
    '''
      This function ask's Server operator to responce
      for sentint to the client.
    '''
    return input("Enter Responce message to send over client side: ")

def send_message_to_client():
    '''
      This function sends message towards the respective client.
    '''
    client[0].send(MESSAGE.encode())

def message_parser(data):
    '''
      This function treams and extracts the message from the returned
      encoded output by client.
    '''
    return str(data)[2:-1]

def recieve_message_from_client():
    '''
      This function looks for the message from the client.
    '''
    return message_parser(client[0].recv(1024))

# Driver code
if __name__ == "__main__":
    s = socket.socket()
    host = socket.gethostname()
    PORT = 8000
    s.bind((host, PORT))
    s.listen(5)
    while True:
        print("Waiting for client connection request...")
        client = client_listener()
        sleep(1)
        print("Connection stablished with client at ", client[1])
        sleep(2)
        MESSAGE = input_message()
        send_message_to_client()
        MESSAGE = recieve_message_from_client()
        sleep(1)
        print("Message sent from Client side: ",MESSAGE)
        sleep(1)
        client[0].close()
        print("Connection closed...")
