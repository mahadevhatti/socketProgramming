import socket

from django.utils.datetime_safe import date

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

s.bind(('localhost', 9999))

print("UDP server up and listening")

while True:
    bytesAddressPair = s.recvfrom(1024)

    print(bytesAddressPair[0].decode())
    date_today = str(date.today())
    s.sendto(bytes(str.encode(date_today)),  bytesAddressPair[1])
