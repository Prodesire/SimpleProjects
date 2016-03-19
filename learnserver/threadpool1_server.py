#coding:utf-8

import sys
import socket
import threading
try:
    import queue as Queue
except ImportError:
    import Queue

server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('0.0.0.0', 8080))
server.listen(32)

response = b'HTTP/1.1 200 OK\r\nConnection: Close\r\nContent-Length: 15\r\n\r\nServer Response'


def handler(queue):
    while True:
        client = queue.get()
        request = client.recv(4096)
        client.send(response)
        client.close()

queue = Queue.Queue()
threads = []

for i in range(4):
    thread = threading.Thread(target=handler, args=(queue,))
    thread.daemon = True
    thread.start()
    threads.append(thread)

while True:
    client, clientaddr = server.accept()
    queue.put(client)