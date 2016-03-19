#coding:utf-8

import sys
import socket
import threading


server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Linux 3.9 or later kernel supports SO_REUSEPORT. Allowing many 
# sockets bind to same ip:port and the kernel distributes the 
# connections to different socket.
# The below line can be only used in Linux.
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
server.bind(('0.0.0.0', 8080))
server.listen(32)

response = b'HTTP/1.1 200 OK\r\nConnection: Close\r\nContent-Length: 15\r\n\r\nServer Response'


def handler():
    while True:
        client, clientaddr = server.accept()
        request = client.recv(4096)
        client.send(response)
        client.close()
    thread.exit()

threads = []

for i in range(4):
    thread = threading.Thread(target=handler, args=())
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()