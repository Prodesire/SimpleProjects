#coding:utf-8
# Only run in Linux

import sys
import socket
import multiprocessing

server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('0.0.0.0', 8080))
server.listen(32)

response = b'HTTP/1.1 200 OK\r\nConnection: Close\r\nContent-Length: 15\r\n\r\nServer Response'


def handler(proc_i):
    while True:
        # print('No.%s handler cicle begin' %proc_i)
        client, addr = server.accept()
        request = client.recv(4096)
        client.send(response)
        client.close()
        # print('No.%s handler cicle end' %proc_i)
    # print('No.%s handler end' %proc_i)
    sys.exit()

processes = []
for i in range(4):
    process = multiprocessing.Process(target=handler, args=(i,))
    process.start()
    processes.append(process)

for process in processes:
    process.join()