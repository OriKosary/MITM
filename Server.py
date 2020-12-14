from socket import socket
from encrypter import Encrypter


class Server:
    def __init__(self, encrypter):
        self.Encrypter = encrypter  # for encryption and decryption has private key and public key

    def send(self, sock, data):  # will always send RSA encrypted
        data = self.Encrypter.encrypt(data)
        sock.send(data)

    def recv(self):  # needs work
        pass

    def main(self, host='127.0.0.2', port=8200):  # client will always send RSA encrypted using this pub_key
        sock = socket()
        sock.bind(('', port))
        try:
            sock.listen(5)
            print('Server started.')
            conn, addr = sock.accept()
            print('Client connected IP:', addr)

            while 'connected':
                data = conn.recv(1024)
                data = data.decode()
                if data == 'close':
                    print("bye")
                    break
                print(data)
        finally:
            sock.close()


e = Encrypter()
s = Server(e)
s.main()
