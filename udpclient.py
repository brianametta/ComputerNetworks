#!/usr/bin/env python
#Briana Wright, CS576 Spring 2017, Program 2 UDP Socket: Client
#client.py
#Connectionless UDP server that connects to a client and adds a "funny" message
#	the server sends the funny message back to the client, client prints message. 

import time
from socket import *

for pings in range(1):
        #Creates internet socket of type UDP
        s = socket(AF_INET, SOCK_DGRAM)
        s.settimeout(2)

        #Address of server
        addr = ("127.0.0.1", 5432)
        message = 'Hello'

        #Sends message to server
        print 'Sending message to server: ',message
        s.sendto(message, addr)

        data, server = s.recvfrom(1024)
        print 'Received following message from server: ', data
