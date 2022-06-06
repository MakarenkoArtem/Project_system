import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 2000))
sock.send(b'OPTIONS')

data = sock.recv(1024)
sock.close()

print(data)