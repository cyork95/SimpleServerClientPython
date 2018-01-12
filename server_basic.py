from socket import *
from select import select

serverPort = 12000
welcomeSocket = socket(AF_INET, SOCK_STREAM)
welcomeSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
welcomeSocket.bind(('',serverPort))
welcomeSocket.listen(5)

while True:
    connectionSocket,addr = welcomeSocket.accept()
    print ("New client from: ", addr)

    while True:
        message = connectionSocket.recv(1024)
        if  message == '':
            print ("Client ",connectionSocket.getpeername(), "closed connection.")
            connectionSocket.close()
            break
        else:
            print (message)
            connectionSocket.sendall(message.upper())


