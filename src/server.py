import socket
from datetime import datetime


sock = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
    socket.IPPROTO_TCP)

address = ('127.0.0.1', 8888)

sock.bind(address)

try:

    sock.listen(1)

    day_time = datetime.now().strftime("%H:%M:%S %d/%m/%Y")

    print(f'--- Starting server on port {address[1]} at {day_time}---')

    conn, addr = sock.accept()

    buffer_length = 8

    message_complete = False

    message = b''

    while not message_complete:
        part = conn.recv(buffer_length)
        message += part
        if len(part) < buffer_length:
            break

    message = message.decode('utf8')

    print(f'[{day_time}] Echoed: {message}')

    message = 'you are connected'

    conn.sendall(message.encode('utf8'))

except KeyboardInterrupt:
    try:
        conn.closed()

    except NameError:

        pass

conn.close()

print(f'--- Stopping server on port {address[1]} at {day_time}---')

sock.close()
