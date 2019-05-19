from socket import *

HOST = '192.168.43.72'
PORT = 65432

# create socket
s = socket(AF_INET, SOCK_STREAM)

# binding socket
s.bind((HOST, PORT))
s.listen(5)

# socket accept
conn, addr = s.accept()
print("Connection has been established! |" + " IP " + addr[0] + " | Port" + str(addr[1]))

# handling client response
while True:
    data = conn.recv(1024)
    print("client : " + data.decode() + "\n" + "waiting client . . . ")
    msg = "message recived."
    conn.send(msg.encode())

conn.close()



