import socket
 
hostname = input("Please enter Hostname: ")
 
# IP lookup from hostname
try:
    ip = socket.gethostbyname(hostname)
    print(f'The {hostname} IP Address is {ip}')
except socket.gaierror as e:
    print(f'Invalid hostname, error raised is {e}')