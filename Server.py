from socket import socket
import select


def send_waiting_messages(wlist, messages_to_send):
    for message in messages_to_send:
        (client_socket, data) = message
        if client_socket in wlist:
            client_socket.send(data)
            messages_to_send.remove(message)


# def data_decode(data):  # need to customize it with the keys
#     name_len = str(data[0])
#     name = str(data[1:int(name_len) + 1])
#     option = str(data[int(name_len)+1])
#     msg = str(data[int(name_len) + 2:])
#     return name_len, name, option, msg
#

def main():
    print("begin server")
    server_socket = socket()

    server_socket.bind(('', 8200))
    server_socket.listen(5)
    open_client_sockets = []
    namesocket = []
    messages_to_send = []

    while True:
        rlist, wlist, xlist = select.select([server_socket] + open_client_sockets, open_client_sockets, [])
        for current_socket in rlist:
            if current_socket is server_socket:
                (new_socket, address) = server_socket.accept()
                print("client connected at", address)
                new_socket.send("test".encode())
                open_client_sockets.append(new_socket)
            else:
                data = current_socket.recv(1024)
                if data == "":
                    open_client_sockets.remove(current_socket)
                    print("Connection with client closed.")
                    for the_socket in open_client_sockets:
                        if the_socket is not current_socket:
                            dc_message = "someone" + " has left the chat!"
                            messages_to_send.append((the_socket, dc_message))
                else:
                    print(data)
                    messages_to_send.append((current_socket, data))

        send_waiting_messages(wlist, messages_to_send)


if __name__ == '__main__':
    main()
