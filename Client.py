from Graphics import *
import threading
from socket import socket
import time
import select
import msvcrt
import encrypter
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP


class Client(GUI):
    def __init__(self, root=None):
        super().__init__(root=root)
        t = threading.Thread(target=self.main)
        t.start()
        e = encrypter.Encrypter()
        self.private_key = e.private_key
        self.public_key = e.public_key
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

    @staticmethod
    def check_recorded(name, keys):
        names = []
        for key in keys: # type -> tuple
            names.append(key(1))  # the name

        if name in names:
            return True

        return False

    def main(self, host='127.0.0.1', port=8200):

        keys = []  # list of tuples key + name of sender
        messages_to_send = []

        name = 'ori'  # input("Enter name : ") TODO: will read from file after login

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
                    rsa_public_key = RSA.importKey(self.public_key)
                    for msg in messages_to_send:  # TODO: I need to add name to send so ill know that key to use
                        if client_socket in wlist:
                            parts = msg.split("->")  # syntax = msg -> user
                            data = ''
                            if self.check_recorded(parts[1]):  # The Key is already in
                                for pair in keys:
                                    if pair[1] == parts[1]:  # the pub_key
                                        temp_key = pair[1]
                                        pub_key = RSA.importKey(temp_key)
                                        pub_key = PKCS1_OAEP.new(pub_key)
                                        data = name + ": " + parts[0]
                                        data = pub_key.encrypt(data.encode())
                            else:  # The Key is not in
                                pass
                                # TODO: this needs to be mirrored in the recv part then i can insert into the key list
                                # like check name in recive in case key not there special msg
                            client_socket.send(data)

                    if client_socket in rlist:
                        data = client_socket.recv(1024)  # need to search here as well for name
                        rsa_private_key = RSA.importKey(self.private_key)
                        rsa_private_key = PKCS1_OAEP.new(rsa_private_key)
                        data = rsa_private_key.decrypt(data)
                        print(data)

        finally:
            client_socket.close()


if __name__ == '__main__':
    root = Tk()
    c = Client(root=root)
    root.mainloop()
