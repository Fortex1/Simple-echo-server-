import socket

sock = socket.socket()
sock.connect(('localhost', 9090))

while True:
    msg = input("you: ")
    sock.send(msg.encode())

    if not msg:  
        break

    data = sock.recv(1024)
    print(data.decode('utf-8'))

sock.close()