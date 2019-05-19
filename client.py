from socket import *

HOST = '192.168.43.72'
PORT = 65432

# create socket
s = socket(AF_INET, SOCK_STREAM)

# connect to server
s.connect((HOST, PORT))

# handling response
while True:
    cmd = input()
    s.send(cmd.encode())
    response = s.recv(1024)
    print("server : " + response.decode())

s.close()