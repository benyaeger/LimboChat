from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('server is up and ready')
while True:
    message, clientAddress = serverSocket.recv(2048)
    print('message {} received from {}'.format(message, clientAddress))
    modifiedMessage = message.decode().upper()
    print('sending server response to {}'.format(clientAddress))
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
