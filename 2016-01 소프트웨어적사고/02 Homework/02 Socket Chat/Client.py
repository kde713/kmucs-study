#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import socket
import security as sec

port = 8888
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


print("===== Socket Chat Client by kde713 =====")
s.connect((input("Input Host Address: "), port))
key = input("Type Security-Key (Server Set): ")

cls()

print("===== Socket Chat Client by kde713 =====")
print()

while 1:
    msg = input(">> ")
    s.send(sec.encrypt(key, msg).encode('utf-8'))
    reply = s.recv(1024)
    if not reply:
        break
    print("Server says '", sec.decrypt(key, reply.decode('utf-8')), "'")

print("(!) Connection Lost")
s.close()