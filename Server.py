from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('Server is up and ready to accept connections on port', serverPort)

while True:
    connectionSocket, clientAddr = serverSocket.accept()
    print('Connection established with {}'.format(clientAddr))
    while True:
        message = connectionSocket.recv(2048).decode()
        if not message:  # Handle client disconnection
            print('Client {} disconnected'.format(clientAddr))
            break
        print('{}: {}'.format(clientAddr, message))
        response = input('Enter response: ')
        connectionSocket.send(response.encode())
