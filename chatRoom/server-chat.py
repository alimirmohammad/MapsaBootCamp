import socket,select
port = 12345
socket_list = []
users = {}
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('',port))
server_socket.listen(5)
socket_list.append(server_socket)
while True:
    ready_to_read,ready_to_write,in_error = select.select(socket_list,[],[],0)
    for sock in ready_to_read:
        if sock == server_socket:
            connect, addr = server_socket.accept()
            socket_list.append(connect)
            connect.send(bytes("You are connected from:" + str(addr), 'utf-8'))
        else:
            try:
                data = sock.recv(2048).decode('utf-8')
                if data.startswith("#"):
                    users[data[1:].lower()]=connect
                    print("User " + data[1:] +" added.")
                    connect.send(bytes("Your user detail saved as : "+str(data[1:]), 'utf-8'))
                elif data.startswith("@"):
                    users[data[1:data.index(':')].lower()].send(bytes(data[data.index(':')+1:], 'utf-8'))
            except:
                continue
server_socket.close()