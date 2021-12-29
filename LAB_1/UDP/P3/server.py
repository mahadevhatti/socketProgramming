import socket


def server_program():
    server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    server_socket.bind(('localhost', 5000))
    print("UDP server up and listening")

    while True:

        bytesAddressPair = server_socket.recvfrom(1024)
        dataSentFromClient = bytesAddressPair[0].decode()
        if not dataSentFromClient:

            break
        print("from connected user: " + str(dataSentFromClient))
        data = input(' -> ')
        server_socket.sendto(data.encode(), bytesAddressPair[1])


if __name__ == '__main__':
    server_program()
