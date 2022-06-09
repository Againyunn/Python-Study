import socket

#서버와 송수신 데이터 크기 지정
bufferSize = 1024
port = 12345
localIP = "127.0.0.1"

#인터넷, UDP프로토콜 설정
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#IP주소와 port 연결(binding)
server_socket.bind((localIP, port))

print("UDP server Waiting for client", port)

while True:
    #client로부터 전달된 값 받기
    received_data = server_socket.recvfrom(bufferSize)  #반환 값: (데이터, IP주소) 
    #received_data[0] = 비트열 데이터, received_data[1] = IP Address

    #str형식으로 디코딩
    data = bytes.decode(received_data[0])

    #입력한 값이 q나 Q면 종료 
    if (data == 'q' or data == 'Q'):
        server_socket.close()
        break
    else:
        print(f'[Client]{data}\n')
    
    #client가 전달한 값을 다시 client로 전달
    server_socket.sendto(data.encode(), received_data[1])
    
server_socket.close()
print("Server Socket Closed")


#처음 짠 코드
# import socket
# from threading import local

# from numpy import byte

# localIP = "127.0.0.1"
# localPort = 12345

# bufferSize = 1024 #담아올 데이터의 버퍼

# UDPServerSocket = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)
# UDPServerSocket.bind((localIP, localPort))

# print("UDP Server Socket UP and Listening")

# while(True):
#     dataPair = UDPServerSocket.recvfrom(bufferSize)

#     message = bytes.decode(dataPair[0]) #데이터
#     address = dataPair[1] #누가 보냈는 지

#     msgFromClient = "Message From Client[{}] {}".format(address, message)

#     print(msgFromClient)

#     msgFromServer1 = "Welcome It's server!"

#     byteToSend1 = str.encode(msgFromServer1)

#     UDPServerSocket.sendto(byteToSend1, address)

#     msgFromServer2 = f"{message}"

#     byteToSend2 = str.encode(msgFromServer2)

#     UDPServerSocket.sendto(byteToSend2, address)