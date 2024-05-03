from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('server is up and ready')
while True:
    message = serverSocket.recv(2048).decode()
    print('message {} received'.format(message))
    modifiedMessage = message.upper()
    print('sending server response...')
    serverSocket.sendto(modifiedMessage.encode())
    print('response sent.')
