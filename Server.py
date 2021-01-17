import socket
import select


def send_waiting_messages(wlist, messages_to_send):
    for message in messages_to_send:
        (client_socket, data) = message
        if client_socket in wlist:
            client_socket.send(data)
            messages_to_send.remove(message)


def data_decode(data):
    name_len = str(data[0])
    name = str(data[1:int(name_len) + 1])
    option = str(data[int(name_len) + 1])
    msg = str(data[int(name_len) + 2:])
    return name_len, name, option, msg


def private_decode(private_msg):
    alphabet = private_msg
    data = alphabet.split(" ", 1)
    print(data[0])
    print(data[1])
    return data[0], data[1]


def main():
    print("begin server")
    server_socket = socket.socket()

    server_socket.bind(('', 8200))
    server_socket.listen(5)
    open_client_sockets = []
    namesocket = []
    messages_to_send = []
    managers = []
    silenced = []

    while True:

        rlist, wlist, xlist = select.select([server_socket] + open_client_sockets, open_client_sockets, [])
        for current_socket in rlist:
            if current_socket is server_socket:
                (new_socket, address) = server_socket.accept()
                print('Client connected IP:', address)
                # new_socket.send("Server says hi".encode())
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

                    for the_socket in open_client_sockets:
                        if the_socket is not current_socket:
                            messages_to_send.append((the_socket, data))  # TODO : found it?!
        send_waiting_messages(wlist, messages_to_send)


if __name__ == '__main__':
    main()
