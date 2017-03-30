#!/usr/bin/env python

#Briana Wright, CS576, Program 1 TCP Socket: Client
#client.py

import socket

#Creates an INET socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = socket.gethostname()
port = 1026

buffer_length = 256
data = "Hello World"

#connect socket to server
s.connect((ip, port))

s.send(data)

#receive data (buffer length) 
r_data = s.recv(buffer_length)

s.close()

print "Received message: ", r_data
