# coding:utf-8

import socket
import threading

server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('0.0.0.0', 8080))
server.listen(32)

response = b'HTTP/1.1 200 OK\r\nConnection: Close\r\nContent-Length: 15\r\n\r\nServer Response'


def handler(client):
    request = client.recv(4096)
    client.send(response)
    client.close()


while True:
    client, addr = server.accept()
    process = threading.Thread(target=handler, args=(client,))
    process.daemon = True
    process.start()
