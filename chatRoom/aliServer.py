import socket
import time
import select
import threading

IP = ''
PORT = 1246

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((IP, PORT))

server_socket.listen(10)
print("server up!")

socket_list = [server_socket]

clients = {}

def check_contact(client_socket, userName, clients):
    while True:
        client_socket.send(bytes("Who do you want to chat with? ", 'utf-8'))
        contact_name = client_socket.recv(1024).decode('utf-8')
        for socket_object in clients:
            if clients[socket_object]["username"] == contact_name:
                contact_socket = socket_object
                break
        else:
            client_socket.send(bytes("This username does not exist!\n", 'utf-8'))
            # print('This username does not exist!')
            continue

        if clients[contact_socket]["status"] == 'offline':
            client_socket.send(bytes("This user is offline!\n", 'utf-8'))
            # print('This user is offline!')
            continue
        # elif clients[contact_socket]["status"] == 'busy':
        #     client_socket.send(bytes("This user is busy!\n", 'utf-8'))
        #     # print('This user is busy!')
        #     continue
        else:
            # return contact_name, contact_socket
            clients[client_socket]["contact_name"] = contact_name
            clients[client_socket]["contact_socket"] = contact_socket
<<<<<<< HEAD
            
            # client_socket.send(bytes(f'You are in PV with {contact_name}', 'utf-8'))
            while True:
                contact_socket.send(bytes(f'{userName} wants to chat with you!\nplease enter {userName}', 'utf-8'))
                temp_name = contact_socket.recv(1024).decode('utf-8')
                if temp_name == userName:
                    clients[contact_socket]["contact_name"] = userName
                    clients[contact_socket]["contact_socket"] = client_socket
                    break

            clients[client_socket]["status"] = 'busy'
            clients[contact_socket]["status"] = 'busy'
            break
        print('===========Thread Script================')
        print(clients)
=======
            clients[contact_socket]["contact_name"] = userName
            clients[contact_socket]["contact_socket"] = client_socket
            client_socket.send(bytes(f'You are in PV with {contact_name}', 'utf-8'))
            contact_socket.send(bytes(f'You are in PV with {userName}', 'utf-8'))
            clients[client_socket]["status"] = 'busy'
            clients[contact_socket]["status"] = 'busy'
            break
>>>>>>> 08d1db03d509d18c3cbf527ab19fea82a87e339e
        # else:
        #     client_socket.send(bytes("This user is busy!\n", 'utf-8'))
        #     print('This user is busy!')
        #     continue

while True:
    read_socket, write_socket, exception_socket = select.select(
        socket_list, [], socket_list)
    for s in read_socket:
        if s == server_socket:
            client_socket, address = server_socket.accept()

            if client_socket:
                client_socket.send(bytes("Welcome! Please enter your username: ", 'utf-8'))
                userName = client_socket.recv(1024).decode('utf-8')
                socket_list.append(client_socket)
                clients[client_socket] = {}
                # t1 = threading.Thread(target=recUsername, args=[s])
                # userName = t1.start()
                
                print(f'{userName} is connected!')
                clients[client_socket]["username"] = userName
                clients[client_socket]["status"] = 'online'
                t = threading.Thread(target = check_contact, args = (client_socket, userName, clients))
                t.start()
<<<<<<< HEAD
                print('===========Main Script================')
                print(clients)
                socket_list.append(client_socket)
=======
>>>>>>> 08d1db03d509d18c3cbf527ab19fea82a87e339e
                # contact_name, contact_socket = check_contact()
                # clients[client_socket]["contact_name"] = contact_name
                # clients[client_socket]["contact_socket"] = contact_socket
                # clients[client_socket]["status"] = 'busy'
                # if clients[client_socket]:
                # clients['username'] = userName
                # print(clients)
                # print("Connection Established from {}".format(address))
                for client_sockets in clients:
                    if client_sockets != client_socket:
                        client_sockets.send(
                            bytes("{} joined Group!".format(userName), 'utf-8'))

        else:
            message = s.recv(1024).decode('utf-8')
            if not message:
                socket_list.remove(s)
                clients[client_socket]["status"] = 'offline'
                continue
            else:
<<<<<<< HEAD
                clients[client_socket]["contact_socket"].send(bytes(message, 'utf-8'))
                print('====================Message=======================')
                print(clients)
=======
                clients[client_socket]["contact_socket"].send(bytes(clients[client_socket]["username"] + "->" + message, 'utf-8'))
>>>>>>> 08d1db03d509d18c3cbf527ab19fea82a87e339e

          #  print(message.decode('utf-8'))
            
    for s in exception_socket:
        socket_list.remove(s)
        clients[client_socket]["status"] = 'offline'
<<<<<<< HEAD
    time.sleep(2)
=======
    time.sleep(5)
>>>>>>> 08d1db03d509d18c3cbf527ab19fea82a87e339e
    # print(socket_list)
server_socket.close()
