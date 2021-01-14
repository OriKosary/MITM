from MITM.Graphics import *
from MITM.encrypter import *
import threading
from socket import socket
import time
import select
import msvcrt
import sys


class Client(GUI):
    def __init__(self, root=None):
        self.e = Encrypter()
        super().__init__(root=root)
        t = threading.Thread(target=self.main)
        t.start()
        # self.main()

    def open_windo(self):
        self.root.mainloop()

    def recvall(self, conn, length):

        buf = b''
        while len(buf) < length:
            data = conn.recv(length - len(buf))
            if not data:
                return data
            buf += data
        return buf

    def main(self, host='127.0.0.1', port=8200):

        keys = []  # list of tuples key + name of sender
        input2 = ""

        while self.wait:
            time.sleep(0.01)
        host = self.input_text

        client_socket = socket()

        # if name not in keys then send the key aswell
        try:
            client_socket.connect((host, port))
            while 'connected':
                rlist, wlist, xlist = select.select([client_socket], [client_socket], [])
                for current_socket in rlist:
                    data = current_socket.recv(1024)
                    data = data.decode()
                    if data != "":
                        print(data)
                    input2 = input("msg : ")
                    current_socket.send(input2.encode())

        finally:
            client_socket.close()


if __name__ == '__main__':
    root = Tk()
    c = Client(root=root)
    root.mainloop()

