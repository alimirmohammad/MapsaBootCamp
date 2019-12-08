from socket import*
from threading import*
IP = '192.168.1.142'
port = 123
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((IP, port))


def send_mes():
    while True:
        mes = input()
        #end_point = input()
        #merg_string = mes+":"+end_point
        if mes:
            client_socket.send(bytes(mes, 'utf8'))


t1 = Thread(target=send_mes)
t1.start()
while True:
    while True:
        recive_mes = client_socket.recv(1024).decode('utf-8')
        print(recive_mes)

    #send_mes = input('->')
    #client_socket.send(bytes(send_mes, "utf-8"))
    #print(client_socket.recv(1024).decode('utf-8'))
    #print(client_socket.recv(1024).decode('utf-8'))
client_socket.close()

