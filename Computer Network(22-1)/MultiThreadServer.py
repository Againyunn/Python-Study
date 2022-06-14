import socket
from _thread import *

server_socket = socket.socket() #기본은 TCP로 설정
host ='localhost' #"127.0.0.1"  #과 동일하다
port = 12345
threadCount = 0
bufferSize = 1024

try:
    #IP주소와 port 연결(binding)
    server_socket.bind((host, port))

except socket.error as e:
    print(str(e))

#client의 connect 요청 대기
print('waiting for a connection...')
server_socket.listen(5)

#client가 connect하면 작동할 client와 통신할 코드
def threaded_client(connection):

    #server와 연결되었음을  client에 전달
    connection.send(str.encode('Welcome to server'))

    while True:
        #client로부터 전달된 값 받기
        data = connection.recv(bufferSize).decode()

        if data=='q' or data=='Q':
            break
        
        else:
            print(f'[Client]{data}')

        #client로부터 전달받은 값을  client에 다시 전달
        connection.send(data.encode())
    
    print("socket closed")
    connection.close()

#코드 본문
while True:
    #client가 connect요청을 하면 연결을 수락하며, client_socket과 client_address 받아서 변수에 저장하기
    client_socket, address = server_socket.accept()

    print('Connected from: '+ address[0] + ':' + str(address[1]))

    #연결된 client별로 thread생성하여 동작
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