#!/usr/bin/env python
#Briana Wright, CS576 Spring 2017, Program 1: TCP Socket
#server.py

import socket

#creates an INET socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if s < 0:
        print 'Socket creation on server failed'

ip = socket.gethostname()
port = 1026

buffer_length = 256

s.bind((ip, port))

s.listen(5)

connection, address = s.accept()

print 'Server will connect to address ', address
while 5:
        r_data = connection.recv(buffer_length)
        if not r_data: break
        print "Received following message: ", r_data

        #Convert data to ascii
        n_data = [ord(i) for i in r_data]

        #Increase ascii number by 1
        fixed_list = [x+1 for x in n_data]

        #Convert back to character
        c_data = [chr(i) for i in fixed_list]

        #Convert array to a string
        final = ''.join(c_data)
        print "New message: ", final
        connection.send(final)
		
connection.close()
