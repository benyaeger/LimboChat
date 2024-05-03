from socket import *

serverName = '10.0.0.15'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Enter string: ')
clientSocket.sendto(message.encode(), (serverName, serverPort))
print('message sent to ({},{})'.format(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recv(2048)
print(modifiedMessage)
clientSocket.close()
