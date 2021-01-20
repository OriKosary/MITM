from Graphics import *
import threading
from socket import socket
import time
import select
import msvcrt


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

        keys = []  # list of tuples key + name of sender
        messages_to_send = []

        name = 'ori'  # input("Enter name : ")

        while self.wait:
            time.sleep(0.01)
        host = self.input_text

        client_socket = socket()

        # if name not in keys then send the key aswell
        try:
            client_socket.connect((host, port))
            print("connected")
            while True:
                while msvcrt.kbhit():
                    print('You: ', end="")
                    msg = ''
                    char = msvcrt.getche().decode()
                    while char != '\r':
                        msg += char
                        char = msvcrt.getche().decode()
                    print('\n')
                    messages_to_send.append(msg)

                while not msvcrt.kbhit():
                    rlist, wlist, xlist = select.select([client_socket], [client_socket], [])
                    for msg in messages_to_send:
                        if client_socket in wlist:
                            client_socket.send((name + ": " + msg).encode())
                            messages_to_send.remove(msg)

                    if client_socket in rlist:
                        data = client_socket.recv(1024)
                        print(data.decode())

        finally:
            client_socket.close()


if __name__ == '__main__':
    root = Tk()
    c = Client(root=root)
    root.mainloop()