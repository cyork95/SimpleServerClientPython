from socket import *

from pip._vendor.distlib.compat import raw_input

serverName = '10.4.82.254'

serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket (AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

while True:
    message = str("Enter message: ")
    clientSocket.sendall(message)
    response = clientSocket.recv(1024)
    print (response)
