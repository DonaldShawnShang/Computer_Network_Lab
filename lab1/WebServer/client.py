#import system specific params
import sys

#import socket module
from socket import *

#determine server name
#local server is set to 127.0.0.1
#replace to your local ip if possible
serverName='127.0.0.1'

#include the port at which the server is listening to 
# port set as 12000 in accordance with server
serverPort=12000

#init the client socket with 2 params
# @param AF_INET address family that is used to determine the type of 
# addresses that the socket can communicate with : IPv4 addresses
# @param SOCK_STREAM connection based protocol commonly used for TCP
clientSocket=socket(AF_INET,SOCK_STREAM)

#connect clientsocket to server name &port
clientSocket.connect((serverName,serverPort))

# assign the sentence to send to have a string with two tokens :
# @token method a request to the server to execute a GET request
# @token file_name the file requested from the server
sentence = sys.argv[1] + ' ' + sys.argv[2]

# send the request to the server
clientSocket.send(sentence.encode('utf-8'))

# init response to store incoming data
response = ''

while True:
    # collect incoming data from clientSocket using .recv()
    # and concatenate it to response. Remember to decode
    # incoming binary data into a string using .decode('utf-8')
    response += clientSocket.recv(1024).decode()
    print(response)
    break

clientSocket.close()






