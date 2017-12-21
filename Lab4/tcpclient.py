#!/usr/bin/python
#Ms. Napatchol Thaipanich 5888205 sec2
#Mr. Arnuphap yupuech 5888236 sec2

import socket  
import time

while True:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    client.connect(('localhost', 13245))
    data = raw_input('Input: ')
    if 'exit' in data:
        break
    else:
        client.send(data)
        t = time.localtime()
        print('... connected from:', socket.gethostbyname('localhost'))
        print time.asctime(t)
        print('received: %s' % client.recv(1024))
client.close() 
