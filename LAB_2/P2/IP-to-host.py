import socket

ipAddress = input("Please enter IP Address : ")

try:
    hostname = socket.gethostbyaddr(ipAddress)
    print(f'The {ipAddress} Hostname is {hostname}')
except socket.herror as e:
    print(f'Invalid hostname, error raised is {e}')