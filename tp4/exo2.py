#!/usr/bin/python3

import socket

def client(host, port):
    sock = socket.socket()
    sock.connect((host, port))
    f = sock.makefile(mode="rw")
    while True:
        chaine = input("entrez une commande: \n")
        f.write(chaine + "\n") 
        f.flush()
        if chaine == "quit":
            break
        else:
            print(f.readline(), end=" ")
    f.close()
    sock.shutdown(socket.SHUT_RDWR)
    sock.close()

client("localhost", 5555)

#"or-iut-i201-f21"