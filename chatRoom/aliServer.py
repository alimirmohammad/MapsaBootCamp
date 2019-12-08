import socket
import time
import select
import threading

IP = ''
PORT = 1268

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((IP, PORT))

server_socket.listen(10)
print("server up!")

socket_list = [server_socket]

clients = {}

def recUsername(s):
    return s.recv(1024)

while True:
    read_socket, write_socket, exception_socket = select.select(
        socket_list, [], socket_list)
    for s in read_socket:
        if s == server_socket:
            client_socket, address = server_socket.accept()

            if client_socket:
                # client_socket.send(bytes("Welcome! Please enter your username: ", 'utf-8'))
                socket_list.append(client_socket)
                ip = address[0]
                clients[client_socket] = [None, None, None]
                clients[client_socket][0] = ip

                # t1 = threading.Thread(target=recUsername, args=[s])
                # userName = t1.start()
                userName = client_socket.recv(1024).decode('utf-8')
                print('username: ', userName)
                clients[client_socket][1] = userName
                clients[client_socket][2] = 'online'
                # clients['username'] = userName
                print(clients)
                print("Connection Established from {}".format(address))
                for client_sockets in clients:
                    if client_sockets != client_socket:
                        client_sockets.send(
                            bytes("{} joined Group!".format(userName), 'utf-8'))

        else:
            message = s.recv(1024)
            if not message:
                socket_list.remove(s)
                del clients[s]
                continue
          #  print(message.decode('utf-8'))
            for client_socket in clients:
                if client_socket != s:
                    client_socket.send(message)
    for s in exception_socket:
        socket_list.remove(s)
        del clients[s]
    time.sleep(5)
    # print(socket_list)
server_socket.close()
