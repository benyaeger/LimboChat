import os
from socket import *

serverPort = int(os.environ.get('PORT', 12000))  # Use Heroku's port or default to 12000 for local testing
serverSocket = socket(AF_INET, SOCK_STREAM)
try:
    serverSocket.bind(('', serverPort))
    serverSocket.listen(1)
    print('Server is up and ready to accept connections on port', serverPort)
except Exception as e:
    print(f'Failed to bind to port {serverPort}: {e}')
    serverSocket.close()
    exit(1)

while True:
    try:
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
    except Exception as e:
        print(f'Error during communication: {e}')
        connectionSocket.close()
        break
