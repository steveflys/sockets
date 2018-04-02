import socket


sock = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
    socket.IPPROTO_TCP)

address = ('127.0.0.1', 8888)

sock.bind(address)

sock.listen(1)

conn, addr = sock.accept()


buffer_length = 8

message_complete = False


while not message_complete:
    part = conn.recv(buffer_length)
    print(part.decode('utf8'))
    if len(part) < buffer_length:
        break

message = 'you are connected'

conn.sendall(message.encode('utf8'))

message_complete = False

while not message_complete:
    part = conn.recv(buffer_length)
    print(part.decode('utf8'))
    if len(part) < buffer_length:
        break

conn.close()

sock.close()
