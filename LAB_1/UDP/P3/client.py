
import socket


def client_program():

    client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    message = input(" -> ")

    while message.lower().strip() != 'bye':
        client_socket.sendto(message.encode(), ('localhost', 5000))
        dataFromServer = client_socket.recvfrom(1024)

        print('Received from server: ' + dataFromServer[0].decode())

        message = input(" -> ")

    client_socket.close()


if __name__ == '__main__':
    client_program()
