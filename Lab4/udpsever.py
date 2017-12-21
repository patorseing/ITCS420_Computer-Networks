#!/usr/bin/python
#Ms. Napatchol Thaipanich 5888205 sec2
#Mr. Arnuphap yupuech 5888236 sec2

import socket

HOST = 'localhost'
PORT = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))

while True:
    print('Waiting for connection . . . ')
    data, address = s.recvfrom(1024)
    print('... connected from:', str(address))
    if data:
        print('received: %s' % data)
        s.sendto(data.upper(), address)
s.close()
