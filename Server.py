from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('server is up and ready')
while True:
    message, clientAddr = serverSocket.recvfrom(2048)
    print('message "{}" received from {}'.format(message.decode(), clientAddr))
    modifiedMessage = message.upper()
    print('sending server response ({}) to {}'.format(modifiedMessage.decode(), clientAddr))
    serverSocket.sendto(modifiedMessage, clientAddr)
    print('response sent.')
