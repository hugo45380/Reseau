import socket
from threading import Thread, Lock
class Server:

    def __init__(self):
        self.counter = 0
        self.lock = Lock()

    def incr(self):
        with self.lock:
            self.counter += 1

    def decr(self):
        with self.lock:
            self.counter -= 1

    def mainServer(self, port):
        sock = socket.socket()
        sock.bind(("0.0.0.0", port))
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.listen(10)
        while True:
            cli, addr = sock.accept()
            sess = Session(self, cli)
            sess.start()



class Session (Thread):

    def __init__(self, server, sock):
        Thread.__init__(self)
        self.server = server
        self.socket = sock
        self.file = sock.makefile(mode="rw")
        

    def run(self):
        while True:
            line = self.file.readline().strip()
            if line == "get":
                with self.server.lock:
                    self.file.write("val %d\n" % self.server.counter)
                self.file.flush()
            elif line == "incr":
                self.server.incr()
                self.file.write("ok\n")
                self.file.flush()
            elif line == "decr":
                self.server.decr()
                self.file.write("ok\n")
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

Server().mainServer(5557)