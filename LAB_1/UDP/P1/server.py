import socket

msgFromServer = "Welcome to the UDP Server"

bytesToSend = str.encode(msgFromServer)


UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
                                 # Internet                 UDP

UDPServerSocket.bind(("127.0.0.1", 20001))

print("UDP server up and listening")


while True:
    bytesAddressPair = UDPServerSocket.recvfrom(1024)

    clientIP = "Client IP Address:{}".format(bytesAddressPair[1])

    print(clientIP)


    UDPServerSocket.sendto(bytes(bytesToSend), bytesAddressPair[1])

