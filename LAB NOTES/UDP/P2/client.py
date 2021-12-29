import socket

c = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

c.sendto(str.encode('What is the date today?'), ('localhost', 9999))

messageFromServer = c.recvfrom(1024)

print("Today's date is : ", messageFromServer[0].decode())
