import socket

s = socket.socket()

s.bind(('localhost', 9899))

s.listen(1)

c, addr = s.accept()

print('Connected with', addr)

c.send(bytes('Welcome to the Server', 'utf-8'))

c.close()
