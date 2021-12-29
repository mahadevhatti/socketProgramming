import socket
from socket import AF_INET, SOCK_STREAM, SO_REUSEADDR, SOL_SOCKET, SHUT_RDWR
import ssl

listen_addr = '127.0.0.1'
listen_port = 8082
server_cert = 'server.crt'
server_key = 'server.key'
client_certs = 'client.crt'

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.verify_mode = ssl.CERT_REQUIRED
context.load_cert_chain(certfile=server_cert, keyfile=server_key)
context.load_verify_locations(cafile=client_certs)

bindsocket = socket.socket()
bindsocket.bind((listen_addr, listen_port))
bindsocket.listen(5)

while True:
    print("Waiting for client")
    newsocket, fromaddr = bindsocket.accept()
    print("Client connected: {}:{}".format(fromaddr[0], fromaddr[1]))
    conn = context.wrap_socket(newsocket, server_side=True)
    print("SSL established. Peer: {}".format(conn.getpeercert()))

    msg = "Welcome to Server!"
    # The system calls send(), sendto(), and sendmsg() are used to transmit a message to another socket.
    conn.send(bytes(msg, 'utf-8'))
    print("Closing connection")
    conn.shutdown(socket.SHUT_RDWR)
    conn.close()
    break
    # buf = b''  # Buffer to hold received client data
    # try:
    #     while True:
    #         data = conn.recv(4096)
    #         if data:
    #             # Client sent us data. Append to buffer
    #             buf += data
    #         else:
    #             # No more data from client. Show buffer and close connection.
    #             print("Received:", buf)
    #             break
    # finally:
