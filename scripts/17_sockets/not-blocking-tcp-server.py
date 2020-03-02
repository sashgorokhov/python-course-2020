import socket, time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind(('localhost', 9999))
sock.listen(1)
sock.setblocking(False)


def handler(client):
    while True:
        try:
            data = client.recv(1024)  # чтение, блокировка​
            if not data:
                break
            udata = data.decode('utf-8')
            client.send(udata.upper().encode('utf-8'))  # запись, блокировка​ ​
        except BlockingIOError:
            continue

    client.close()


while True:
    try:
        client, addr = sock.accept()      # неблокирующий вызов​
        print('Connected: ', addr)
        break
    except socket.error:        # отсутствие подключения​
        print('Waiting for connection...')

        time.sleep(1)


handler(client)
