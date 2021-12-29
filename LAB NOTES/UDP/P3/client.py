
import socket


def client_program():

    client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)  # instantiate

    message = input(" -> ")  # take input

    while message.lower().strip() != 'bye':
        client_socket.sendto(message.encode(), ('localhost', 5000))
        dataFromServer = client_socket.recvfrom(1024)  # receive response

        print('Received from server: ' + dataFromServer[0].decode())  # show in terminal

        message = input(" -> ")  # again take input

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()
