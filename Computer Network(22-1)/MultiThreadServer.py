import socket
from _thread import *

server_socket = socket.socket()
host ='localhost'
port = 12345
threadCount = 0

try:
    server_socket.bind((host, port))

except socket.error as e:
    print(str(e))

print('waiting for a connection...')
server_socket.listen(5)


def threaded_client(connection):
    connection.send(str.encode('Welcome to server'))
    while True:
        data = connection.recv(2048)
        str_data = data.decode()

        if str_data=='q' or str_data=='Q':
            break
        
        else:
            print(str(data))
    
    print("socket closed")
    connection.close()

while True:
    client_socket, address = server_socket.accept()

    print('Connected from: '+ address[0] + ':' + str(address[1]))

    start_new_thread(threaded_client,(client_socket,))

    threadCount += 1
    print('Thread Number: '+str(threadCount))

server_socket.close()


# 교수님 코드
# import socket
# from _thread import *

# server_socket = socket.socket()
# host = 'localhost'
# port = 12345
# threadCount = 0

# try:
#     server_socket.bind((host, port))
# except socket.error as e:
#     print(str(e))
    
# print('waiting for a connection...')
# server_socket.listen(5)
# def threaded_client(connection):
#     connection.send(str.encode('Welcom to the server'))
#     while True:
#         data = connection.recv(512).decode()
#         if (data == 'q' or data == 'Q'):
#             break
#         else:
#             print(data)
    
#     print("socket closed")
#     connection.close()
# while True:
#     client_socket, address = server_socket.accept()
    
#     print('Connected from: ' + address[0] + ':' + str(address[1]))
    
#     start_new_thread(threaded_client,(client_socket, ))
    
#     threadCount += 1
#     print('Thread Number: ' + str(threadCount))
    
# server_socket.close()