import socket

c = socket.socket()

c.connect(('localhost', 9899))

print(c.recv(1024).decode())