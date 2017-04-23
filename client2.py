from socket import *


#serverName = '10.4.82.254'

serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

while True:
    message = input("Enter message: ")
    clientSocket.sendall(message.encode('utf-8'))
    response = clientSocket.recv(1024)
    print(response)
    if message == '#':
        print("You have closed the connection.")
        break
