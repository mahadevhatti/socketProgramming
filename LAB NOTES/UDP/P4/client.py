import socket

from distlib.compat import raw_input

client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
port = 9999



# receive and send message from/to different user/s

while True:
    # send user details to server
    send_msg = raw_input("Enter your user name(prefix with #):")
    client_socket.sendto(bytes(send_msg, 'utf-8'), ('localhost', 9999))

    # receive connection message from server
    dataFromServer = client_socket.recvfrom(1024)
    print(dataFromServer[0].decode())

    dataFromCl = client_socket.recvfrom(1024)
    print(dataFromCl[0].decode())
    send_msg = raw_input("Send your message in format [@user:message] ")
    if send_msg == 'exit':
        break
    else:
        client_socket.sendto(bytes(send_msg, 'utf-8'), ('localhost', 9999))

client_socket.close()
