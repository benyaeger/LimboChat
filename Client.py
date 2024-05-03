from socket import *

serverName = '10.0.0.15'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
print('connection has been established with {}'.format((serverName, serverPort)))
while True:
    message = input('Enter string: ')
    print('Sending message to ({},{})...'.format(serverName, serverPort))
    clientSocket.send(message.encode())
    print('message sent to ({},{})'.format(serverName, serverPort))
    modifiedMessage = clientSocket.recv(2048)
    print('{} responded: {}'.format((serverName, serverPort), modifiedMessage.decode()))
# clientSocket.close()
