import socket

serverAddressPort = ("127.0.0.1", 20001)


UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPClientSocket.sendto(str.encode(''), serverAddressPort)

msgFromServer = UDPClientSocket.recvfrom(1024)

msg = "Message from Server :  {}".format(msgFromServer[0].decode())

print(msg)
