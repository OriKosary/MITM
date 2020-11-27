from ProjectMITM.Graphics import *
import threading
from socket import socket
import time


class Client(GUI):
    def __init__(self, root=None):
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

        while self.wait:
            time.sleep(0.01)
        host = self.input_text
        sock = socket()

        try:
            sock.connect((host, port))
            while 'connected':
                data = input("Enter msg: ").encode()
                sock.send(data)
        finally:
            sock.close()


if __name__ == '__main__':
    root = Tk()
    c = Client(root=root)
    # c.main()
    root.mainloop()
