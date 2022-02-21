import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),1234))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been estabilished")
    clientsocket.send(bytes("Selamat Datang di Server ", "utf-8"))
    clientsocket.close()