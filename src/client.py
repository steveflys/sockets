import socket

infos = socket.getaddrinfo('127.0.0.1', 8888)

stream_info = [i for i in infos if i[1] == socket.SOCK_STREAM][0]

stream_info

client = socket.socket(*stream_info[:3])

client.connect(stream_info[-1])

message = 'Open the pod bay doors hal'

client.sendall(message.encode('utf8'))

buffer_length = 8

message_complete = False

while not message_complete:
    part = client.recv(buffer_length)
    print(part.decode('utf8'))
    if len(part) < buffer_length:
        break

client.close()

