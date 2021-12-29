import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 7655))
server.listen(5)

clients = []
nicknames = []
passwords = {}
clientSockets = {}


def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clientSockets.pop(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} left!'.format(nickname).encode('ascii'))
            nicknames.remove(nickname)
            break


def receive():
    while True:
        client, address = server.accept()
        print("Connected with {}".format(str(address)))
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        passwordfromCl = client.recv(1024).decode('ascii')
        if nickname in nicknames:
            if passwords[nickname] == passwordfromCl:
                client.send('Welcome Back to the Conference!'.encode('ascii'))
                clients.append(client)
                clientSockets[client] = nickname
                print("Username is {}".format(nickname))
                broadcast("{} joined!".format(nickname).encode('ascii'))
                client.send('Connected to Server!'.encode('ascii'))

                thread = threading.Thread(target=handle, args=(client,))
                thread.start()
            else:
                client.send('Wrong Password!'.encode('ascii'))
        else:
            passwords[nickname] = passwordfromCl
            nicknames.append(nickname)
            clients.append(client)
            clientSockets[client] = nickname
            print("Username is {}".format(nickname))
            broadcast("{} joined!".format(nickname).encode('ascii'))
            client.send('Connected to Server!'.encode('ascii'))

            thread = threading.Thread(target=handle, args=(client,))
            thread.start()



print('Server is Listening')
receive()
