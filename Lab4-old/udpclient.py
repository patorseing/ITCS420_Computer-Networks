#!/usr/bin/python
#Ms. Napatchol Thaipanich 5888205 sec2
#Mr. Arnuphap yupuech 5888236 sec2

import socket
import time

HOST = 'localhost'
PORT = 8000

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = raw_input('Input: ')
    s.sendto(data.encode(), (HOST, PORT))
    if 'exit' in data:
        break
    else:
        t = time.localtime()
        print('... connected from:', socket.gethostbyname('localhost'))
        print time.asctime(t)
        data, address = s.recvfrom(1024)
        print('received: %s' % data)
s.close()
