import socket

class Server:

    def __init__(self):
        self.counter = 0

    def incr(self):
        self.counter += 1

    def mainServer(self, port):
        sock = socket.socket()
        sock.bind(("0.0.0.0", port))
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.listen(10)
        while True:
            cli, addr = sock.accept()
            sess = Session(self, cli)
            sess.mainSession()


class Session:

    def __init__(self, server, sock):
        self.server = server
        self.socket = sock
        self.file = sock.makefile(mode="rw")

    def mainSession(self):
        while True:
            line = self.file.readline().strip()
            if line == "get":
                self.file.write("val %d\n" % self.server.counter)
                self.file.flush()
            elif line == "incr":
                self.server.incr()
                self.file.flush()
            elif line == "decr":
                self.server.incr()
                self.file.flush()
            elif line == "quit":
                self.file.write("quit\n")
                self.file.flush()
                break
            else:
                self.file.write("err\n")
                self.file.flush()
        self.file.close()
        self.socket.shutdown(socket.SHUT_RDWR)
        self.socket.close()

Server().mainServer(5555)