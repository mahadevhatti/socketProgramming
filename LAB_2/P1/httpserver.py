from socket import (
    socket, 
    AF_INET, 
    SOCK_STREAM,
    SO_REUSEADDR,
    SOL_SOCKET
)

HOST, PORT = "localhost", 8080
response = b"HTTP/1.1 200 OK\n\n hi hello from Mahadev Hatti"


with socket(AF_INET, SOCK_STREAM) as sock:
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind((HOST, PORT))
    sock.listen(1)
    while True:
        try:
            conn, addr = sock.accept()
            req = conn.recv(1024).decode()
            print(req)
            conn.sendall(response)
            conn.close()
        except Exception as E:
            print(E)