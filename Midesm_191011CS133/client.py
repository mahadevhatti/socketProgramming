import socket

from distlib.compat import raw_input


def client_program():
    client_socket = socket.socket()
    client_socket.connect(('localhost', 5000))

    message = []

    loopingNo = 1

    while loopingNo != 0:

        n = int(input("\n\tEnter the list size : "))
        for i in range(0, n):
            print("Enter string at index : ", i, )
            item = (input())
            message.append(item)

        dataFromClient = str(message)
        dataFromClient = dataFromClient.encode()
        client_socket.send(dataFromClient)
        print('Data has been successfully sent to server\n')

        dataFromServer = client_socket.recv(1024).decode()
        dataFromServer = eval(dataFromServer)
        print("\n\t\tData Received from Server : ")
        for x in dataFromServer:
            print(x)

    client_socket.close()


if __name__ == '__main__':
    client_program()
