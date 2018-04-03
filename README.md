# sockets

# client = socket.socket(*stream_info[:3])
# client
# client.connect(stream_info[-1])
# message = 'This is awesome. I am a client sending data to my server'
# client.sendall(message.encode('utf8'))
# conn.send?
# conn.send??
# buffer_length = 8
# message_complete = False

# while not message_complete:
#     part = client.recv(buffer_length)
#     print(part.decode('utf8'))
#     if len(part) < buffer_length:
#         break
# client.close()
# history


# conn

# addr

# buffer_length = 8

# message_complete = False

# while not message_complete:
#     part = conn.recv(buffer_length)
#     print(part.decode('utf8'))
#     if len(part) < buffer_length:
#         break
# message = 'you are connected'

# conn.sendall(message.encode('utf8'))

# conn.send??

# conn.sendall??
# while not message_complete:
#     part = conn.recv(buffer_length)
#     print(part.decode('utf8'))
#     if len(part) < buffer_length:
#         break
# conn.close()
# sock.close()
# history