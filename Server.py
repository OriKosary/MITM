from socket import socket

def main(host='127.0.0.2', port=8200):
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


if __name__ == '__main__':
    main()