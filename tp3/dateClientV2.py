#!/usr/bin/python3

import socket
import sys


BUFSIZE = 1024

def client ( host , port ):
    sock = socket.socket(type=socket.SOCK_DGRAM)
    addr = (host, port)
    sock.sendto(b"user"+b" Jolan est homo", addr) # ou bien sock.sendto(b"date", addr)
    data = sock.recv(BUFSIZE)
    print(data.decode(), end="")

client(sys.argv[1], 5555) # [0] le nom de la fonction, [1] le premier argument