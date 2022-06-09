import socket

#서버와 송수신 데이터 크기 지정
bufferSize = 1024
port = 12345
localIP = "127.0.0.1"

#인터넷, TCP프로토콜 설정
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#IP주소와 port 연결(binding)
server_socket.bind((localIP, port))

#client의 connect 요청 대기
server_socket.listen(5)

print("TCP server Waiting for client", port)

#client가 connect요청을 하면 연결을 수락하며, client_socket과 client_address 받아서 변수에 저장하기
client_socket, client_address = server_socket.accept() #listen에 사용하는 소켓, 통신에 사용하는 소켓이 다르다.
print("connect from ", client_address)

##TCP는 listen -> connect -> accept 순서로 이미 상호간의 포트 연결이 되어있으므로,
##매번의 send/recv 시 포트번호를 명시할 필요가 없다.
##그냥 데이터 값만 넣으면 된다.
while True:
    #client로부터 전달된 값 받기
    data = client_socket.recv(port).decode() #.recv 반환 값: 비트열 데이터 -> .decode: 문자열 데이터
    
    if data == 'q' or data == 'Q': #client가 q나 Q를 보내서 server가 받으면 꺼진다.
        client_socket.close()
        break
    
    else: #q나 Q 이외의 값이 넘어오면 출력
        print(f'[Client]{data}\n')
    
    #client로부터 전달받은 값을  client에 다시 전달
    client_socket.send(data.encode())


server_socket.close()
print("Server Socket Closed")