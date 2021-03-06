import socket
import sys

infos = socket.getaddrinfo('127.0.0.1', 8888)

stream_info = [i for i in infos if i[1] == socket.SOCK_STREAM][0]
# could do this instead:
# for sock_data in infos:
#     if sock_data[1] == socket.SOCK_STREAM:
#         stream_info =sock_data # 5-tuple repr of socket

# 5-tuple repr of socket =>
stream_info

client = socket.socket(*stream_info[:3])
#above same as:
# client = socket.socket(
#   stream_info[0], # Family
#   stream_info[1], # Kind
#   stream_info[2]' # Protocol
# )

client.connect(stream_info[-1])

#message = sys.argv[1]

message = 'Open the pod bay doors hal'

client.sendall(message.encode('utf8'))

buffer_length = 8

message_complete = False

message_parts = []

while not message_complete:
    part = client.recv(buffer_length)
    message_parts.append(part)
    if len(part) < buffer_length:
        break

message_final = b''

bit_message = message_final.join(message_parts)

message_out = bit_message.decode('utf8')

print(message_out)

client.close()

