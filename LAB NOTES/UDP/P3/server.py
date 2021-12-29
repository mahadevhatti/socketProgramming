import socket


def server_program():
    server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind(('localhost', 5000))  # bind host address and port together
    print("UDP server up and listening")

    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        bytesAddressPair = server_socket.recvfrom(1024)
        dataSentFromClient = bytesAddressPair[0].decode()
        if not dataSentFromClient:
            # if data is not received break
            break
        print("from connected user: " + str(dataSentFromClient))
        data = input(' -> ')
        server_socket.sendto(data.encode(), bytesAddressPair[1])  # send data to the client


if __name__ == '__main__':
    server_program()
