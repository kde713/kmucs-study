#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import security as sec
import makereply as mr

port = 8888
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('', port))
s.listen(1)

print("## Host:", socket.gethostbyname(socket.getfqdn()))

key = input("Enter Security-Key: ")

print("Log) Socket Listen Started.")

connector, addr = s.accept()

while 1:
    msg = connector.recv(1024)
    if not msg:
        break
    print("Log) Message Received: ", msg.decode('utf-8'))
    print("Log) Decrypted: ", sec.decrypt(key, msg.decode('utf-8')))
    reply = mr.echo(sec.decrypt(key, msg.decode('utf-8')))
    connector.send(sec.encrypt(key, reply).encode('utf-8'))

s.close()