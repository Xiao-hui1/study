from socket import *

s = socket()

s.connect(('127.0.0.1', 8080))


while True:
    text = s.recv(1024).decode('utf-8')
    print(text)
    command = input('Enter command: ')
    s.send(command.encode('utf-8'))

