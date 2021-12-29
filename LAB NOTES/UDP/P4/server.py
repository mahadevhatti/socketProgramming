import select
import socket

port = 9999
socket_list = []
users = {}
server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
                            # IP4 internet family     SOCK_DGRAM (for UDP)

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', port))
print("UDP server up and listening")

socket_list.append(server_socket)

while True:
    for sock in socket_list:
        if sock == server_socket:
            bytesAddressPair = server_socket.recvfrom(1024)
            socket_list.append(bytesAddressPair[1])
            server_socket.sendto(bytes("You are connected from:" + str(bytesAddressPair[1]), 'utf-8'),  bytesAddressPair[1])
        else:
            # noinspection PyBroadException
            try:
                dataSentFromClient = sock.recvfrom(2048)
                data = dataSentFromClient[0].decode()
                if data.startswith("#"):
                    # noinspection PyUnboundLocalVariable
                    users[data[1:].lower()] = bytesAddressPair[1]
                    print("User " + data[1:] + " added.")
                    server_socket.sendto(bytes("Your user detail saved as : " + str(data[1:]), 'utf-8'), bytesAddressPair[1])
                elif data.startswith("@"):
                    server_socket.sendto(bytes(data[data.index(':') + 1:], 'utf-8'),users[data[1:data.index(':')].lower()])
            except:
                continue

