#coding:utf-8
# Only run in Linux

import os, sys
import fcntl
import socket
import select


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
    read_list = clients.copy()
    read_list.add(server)

    read_list, write_list, error_list = select.select(read_list, [], [], 10)

    for fd in read_list:
        if fd == server:
            client, clientaddr = server.accept()
            clients.add(client)
        else:
            request = fd.recv(4096)
            fd.send(response)
            clients.remove(fd)
            fd.close()