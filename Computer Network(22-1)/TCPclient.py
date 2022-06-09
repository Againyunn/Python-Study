import socket

#서버와 송수신 데이터 크기 지정
bufferSize = 1024
port = 12345
localIP = "127.0.0.1"

#인터넷, TCP프로토콜 설정
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#IP주소와 port 연결(binding)
client_socket.connect((localIP, port))


##TCP는 listen -> connect -> accept 순서로 이미 상호간의 포트 연결이 되어있으므로,
##매번의 send/recv 시 포트번호를 명시할 필요가 없다.
##그냥 데이터 값만 넣으면 된다.
while True:
    #화면에 인터페이스 출력
    data = input("SEND( type q or Q to Quit :")

    #사용자로부터 입력받은 값을  server로 전달
    client_socket.send(data.encode())
    
    #입력한 값이 q나 Q면 종료 
    if data == 'q' or data == 'Q':
        client_socket.close()
        break
    
    #server로부터 전달된 값 받기
    data = client_socket.recv(port).decode() #.recv 반환 값: 비트열 데이터 -> .decode: 문자열 데이터



    print(f'[Server]{data}\n')

print("socket closed")