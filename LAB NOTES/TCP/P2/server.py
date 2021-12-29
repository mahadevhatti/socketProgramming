import socket

from django.utils.datetime_safe import date

s = socket.socket()

s.bind(('localhost', 9999))

s.listen(1)

while True:
    c, addr = s.accept()
    print('Connected with', addr)

    que = c.recv(1024).decode()
    print(que)
    date_today = str(date.today())
    # c.send(bytes(date_today.encode()))
    c.send(bytes(date_today, 'utf-8'))
    c.close()
