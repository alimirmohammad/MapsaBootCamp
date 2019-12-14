import socket
import time
import select

IP = 'localhost'
PORT = 8201

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((IP, PORT))

server_socket.listen(10)
print("server up!")

socket_list = [server_socket]

clients = {}
users = {}
# usernames = []


while True:
    read_socket, write_socket, exception_socket = select.select(
        socket_list, [], socket_list)
    for s in read_socket:
        if s == server_socket:
            client_socket, address = server_socket.accept()
            if client_socket:
                username = client_socket.recv(1024).decode('utf-8')
                client_socket.send(bytes("welcome! {}\n".format(username), 'utf-8'))
                socket_list.append(client_socket)
                user = str(address[0]) + str(address[1])
                clients[client_socket] = user
                users[user] = {'status': 'connected', 'chatTo': None, 'username': username}
                # usernames.append(username)
                print("Connection Established from {}".format(address))
                client_socket.send(bytes("Who do you want to chat to?", 'utf-8'))
                for client_sockets in clients:
                    if client_sockets != client_socket:
                        client_sockets.send(
                            bytes("{} joined Group with address {}".format(username, address), 'utf-8'))

        else:
            message = s.recv(1024).decode('utf-8')
            if not message:
                socket_list.remove(s)
                del clients[s]
                continue
            if message[0] == '#':
                if message == '#finish':
                    u = clients[s]
                    users[u]['status'] = 'connected'
                    u2 = users[u]['chatTo']
                    users[u]['chatTo'] = None
                    name1 = users[u]['username']
                    for user in users:
                        if users[user]['chatTo'] == s:
                            users[user]['status'] = 'connected'
                            users[user]['chatTo'] = None
                            name2 = users[user]['username']
                    finished_message = bytes('#finishPrivate chat is finished\nNow you can choose another user',
                                             'utf-8')
                    s.send(finished_message)
                    u2.send(finished_message)
                    print('A chat is finished between {} and {}'.format(name1, name2))
                else:
                    message = message[1:].split('->')
                    sender_user = message[0]
                    receiver_user = message[1]
                    for u in users:
                        if users[u]['username'] == receiver_user:
                            if users[u]['status'] == 'busy':
                                s.send(bytes("#busy", 'utf-8'))
                            elif users[u]['status'] == 'disconnected':
                                s.send(bytes("#disconnect", 'utf-8'))
                            else:
                                users[u]['status'] = 'busy'
                                users[u]['chatTo'] = s
                                for us in users:
                                    if users[us]['username'] == sender_user:
                                        users[us]['status'] = 'busy'
                                for client_socket in clients:
                                    if clients[client_socket] == u:
                                        for usr in users:
                                            if users[usr]['username'] == sender_user:
                                                users[usr]['chatTo'] = client_socket
                                        s.send(bytes("#OK", 'utf-8'))
                                        client_socket.send(bytes("#OK", 'utf-8'))
                                        print('A chat is established between {} and {}'.format(sender_user,
                                                                                               receiver_user))
                            break
                    else:
                        s.send(bytes('#exist', 'utf-8'))
            else:
                for user in users:
                    if users[user]['chatTo'] == s:
                        for cl in clients:
                            if clients[cl] == user:
                                receiver_socket = cl
                                receiver_socket.send(bytes(message, 'utf-8'))
                                break
                        break
    for s in exception_socket:
        socket_list.remove(s)
        del clients[s]
    # print(socket_list)
# server_socket.close()
