from socket import *
from select import select

serverPort = 12000
welcomeSocket = socket(AF_INET, SOCK_STREAM)
welcomeSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
welcomeSocket.bind(('',serverPort))
welcomeSocket.listen(5)

rlist = [welcomeSocket];

while True:
    readable, writable, exceptional = select (rlist, [], []);

    for s in readable:

        if s is welcomeSocket:
            connectionSocket,addr = welcomeSocket.accept()
            print ("New client from: ", addr)
            rlist.append(connectionSocket)

        else:
            message = s.recv(1024)
            if  message == '':
                print ("Client ",s.getpeername(), "closed connection.")
                s.close()
                rlist.remove(s)

            else:
                print (message)
                s.sendall(message.upper())
#                s.close()
#                rlist.remove(s)

