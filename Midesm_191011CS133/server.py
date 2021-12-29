import socket


def server_program():
    server_socket = socket.socket()

    server_socket.bind(('localhost', 5000))

    server_socket.listen(2)
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        data = eval(data)
        dataToClient = data.copy()
        dataToClient.sort()
        dataToClient = str(dataToClient)
        dataToClient = dataToClient.encode()
        conn.send(dataToClient)

    conn.close()


if __name__ == '__main__':
    server_program()
