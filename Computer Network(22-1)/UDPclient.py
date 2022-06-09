import socket

#인터넷, UDP프로토콜 설정
client_socket =socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#서버와 송수신 데이터 크기 지정
serverAddress = ("127.0.0.1", 12345)
bufferSize = 1024

while True:
    #화면에 인터페이스 출력
    data = input("SEND( type q or Q to Quit) :")

    #사용자로부터 입력받은 값을  server로 전달
    client_socket.sendto(data.encode(), serverAddress)

    #입력한 값이 q나 Q면 종료 
    if(data == 'q' or data == 'Q'):
        client_socket.close()
        break
    
    #server로부터 전달된 값 받기
    received_data = client_socket.recvfrom(bufferSize)  #반환 값: (데이터, IP주소) 
    #received_data[0] = 비트열 데이터, received_data[1] = IP Address

    #str형식으로 디코딩
    data = bytes.decode(received_data[0])

    print(f'[Server]{data}\n')


print("socket closed")


#처음 짠 코드
# import socket

# msgFromClient = ">>>client: Hello Computer Network"
# byteToSend = str.encode(msgFromClient)
# bufferSize = 1024
# serverAddress = ("127.0.0.1", 12345)

# #인터넷+ UDP형식의 통신 프로토콜로 socket 설정
# UDPClientSocket = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)

# #server에 
# UDPClientSocket.sendto(byteToSend, serverAddress)

# for i in range(2):
#     msgFromServer = UDPClientSocket.recvfrom(bufferSize)

#     decodedMsg = bytes.decode(msgFromServer[0])

#     msg = f"Message from Server {decodedMsg}"
#     print(msg)