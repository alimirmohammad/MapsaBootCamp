import socket
import time
import sys
import threading

IP = 'localhost'
PORT = 8201
username = input("Enter your name: ")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
client_socket.send(bytes(username, 'utf-8'))
isChosen = False


def send_message():
    while True:
        global isChosen
        msg = input()
        if msg:
            if not isChosen:
                msg = '#' + username + '->' + msg
                isChosen = True
            elif msg == 'finish':
                msg = '#finish'
            else:
                msg = username + "->" + msg
            client_socket.send(bytes(msg, 'utf-8'))


def first_setup():
    mess = client_socket.recv(2048)
    print(mess.decode('utf-8'))
    client_socket.setblocking(0)


t1 = threading.Thread(target=send_message)
t1.start()


first_setup()
while True:
    # #    message = client_socket.recv(1024)
    # #    print(message.decode('utf-8'))
    # msg = input('{}-> '.format(username))
    # if msg:
    #     client_socket.send(bytes(username + "->" + msg, 'utf-8'))

    try:
        while True:
            message = client_socket.recv(1024)
            if not message:
                print("Connection Closed!")
                sys.exit()
            message = message.decode('utf-8')
            if message == '#OK':
                print("Now you can start messaging")
                print("If you want to close this private chat enter finish")
                isChosen = True
            elif message == '#busy':
                print('Username you chose was busy')
                isChosen = False
            elif message == '#disconnect':
                print('Username you chose was disconnected')
                isChosen = False
            elif message == '#exist':
                print('Username does not exist')
                isChosen = False
            elif message[:7] == '#finish':
                print('finish')
                print(message[7:])
                isChosen = False
            else:
                print(message)

    except IOError as e:
        pass

#    time.sleep(5)
