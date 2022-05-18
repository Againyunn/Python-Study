import socket

port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', port))
server_socket.listen(5)

print("TCP server Waiting for client", port)


client_socket, client_address = server_socket.accept() #listen에 사용하는 소켓, 통신에 사용하는 소켓이 다르다.
print("connect from ", client_address)

while True:
    data = client_socket.recv(512).decode() #받아온 숫자를 문자로 변환하여 data에 저장
    
    if data == 'q' or data == 'Q': #client가 q나 Q를 보내서 server가 받으면 꺼진다.
        client_socket.close()
        break
    
    else: #q나 Q 이외의 값이 넘어오면 출력
        print(data)

server_socket.close()
print("Server Socket Closed")