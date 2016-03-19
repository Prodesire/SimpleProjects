# coding:utf-8

import socket

# server, the socket object of server
server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('0.0.0.0', 8080))
# listen create a received queue. 32 represents allowed waiting connections number.
server.listen(32)

response = b'HTTP/1.1 200 OK\r\nConnection: Close\r\nContent-Length: 15\r\n\r\nServer Response'

while True:
    #client, the socket object of client
    #clientaddr, the address of client. Format seems like (ip, port)
    client, clientaddr = server.accept() # blocking
    #request, client's request
    request = client.recv(4096) # blocking
    # print(request, clientaddr)
    client.send(response) # maybe blocking
    client.close()