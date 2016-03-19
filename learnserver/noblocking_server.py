#coding:utf-8
# Only run in Linux

import os, sys
import fcntl
import socket


server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('0.0.0.0', 8080))
server.listen(32)

# enable noblocking
flags = fcntl.fcntl(server.fileno(), fcntl.F_GETFL)
fcntl.fcntl(server.fileno(), fcntl.F_SETFL, flags | os.O_NONBLOCK)

response = b'HTTP/1.1 200 OK\r\nConnection: Close\r\nContent-Length: 15\r\n\r\nServer Response'


clients = set([])

while True:
    try:
        # under the noblocking mode, accept() and recv() func will
        # return EAGAIN or EWOULDBLOCK exception if there is no usable data.
        client, clientaddr = server.accept()
        clients.add(client)
    except Exception as e:
        pass

    for client in clients.copy():
        try:
            request = client.recv(4096)
            client.send(response)
            client.remove(client)
            client.close()
        except Exception as e:
            pass