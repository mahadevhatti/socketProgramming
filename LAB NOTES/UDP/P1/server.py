import socket

msgFromServer = "Welcome to the UDP Server"

bytesToSend = str.encode(msgFromServer)

# Create a datagram socket

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
                                 # Internet                 UDP
# Bind to address and ip

UDPServerSocket.bind(("127.0.0.1", 20001))

print("UDP server up and listening")

# Listen for incoming datagrams

while True:
    bytesAddressPair = UDPServerSocket.recvfrom(1024)

    clientIP = "Client IP Address:{}".format(bytesAddressPair[1])

    print(clientIP)

    # Sending a reply to client

    UDPServerSocket.sendto(bytes(bytesToSend), bytesAddressPair[1])

