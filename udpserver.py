#!/usr/bin/env python
#Briana Wright, CS576 Spring 2017, Program 2 UDP Socket Server
#server.py
#Connectionless UDP server that connects to a client and adds a "funny" message
#	the server sends the funny message back to the client, client prints message. 

import socket

funny = ' -Destroy all humans'

#Creates an INET socket of type UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Address of client
address = ("127.0.0.1", 5433)
ip = "127.0.0.1"
port = 5432

s.bind((ip, port))

while True:
        message, address  = s.recvfrom(1024)
        print 'Received message: ', message
        message = message + funny
        s.sendto(message, address)
        print 'Sending message: ', message
