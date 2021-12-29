import socket

c = socket.socket()

c.connect(('localhost', 9999))

c.send(bytes('What is the date today?', 'utf-8'))

print("Today's date is : ", c.recv(1024).decode())
