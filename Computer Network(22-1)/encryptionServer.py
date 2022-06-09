import socket
from _thread import *
from time import sleep

from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad

key = '!!12345678900987654321!!12345678'
iv = '1234567890123456'
decipher = AES.new(key.encode(), AES.MODE_CBC, iv.encode())
cipher = AES.new(key.encode(), AES.MODE_CBC, iv.encode())

#TCP로 통신하도록 socket설정
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 12345
threadCount = 0



#소켓과 연결(bind)하고, 예외 발생 시 화면에 출력하도록 설정
try:
    server_socket.bind((host, port))
except socket.error as e:
    print(str(e))

#client의 connect신호를 대기
server_socket.listen(5)

#################################################################
#client와 연결되면 thread가 생성되며 아래의 함수 실행
def threaded_client(connection):
    
    while True:
        ######################################################
        #전달받은 데이터 해독(client -> server)
        data = connection.recv(4096) #최대 4096bit까지 수신가능
        print("recieved  : ", data) #client가 전송한 data 원본

        #복호화1(decrypted)
        decrypted_data = decipher.decrypt(data)
        print("decrypted : ", decrypted_data)
        
        #복호화2(decrypted 된 데이터를 unpad처리)
        unpadded_data = unpad(decrypted_data, AES.block_size)
        print("unpadded  : ", unpadded_data)
        print(unpadded_data[0])
        print(unpadded_data[1])

        #디코딩(unpad된 데이터를 decoding)
        decoded_data = unpadded_data.decode() #각 내용이 ,로 구분되어서 디코딩
        print("decoded   : ", decoded_data)
        print(decoded_data[0])
        print(decoded_data[1])
        
        #,를 기준으로 데이터를 분류
        parsed_data = decoded_data.split(',')
        print(parsed_data[0])
        print(parsed_data[1])
        print(parsed_data[2])
        print(parsed_data[3])
        print(parsed_data[4]) #사용자 입력부분
        
        #사용자 입력이 'q'이면 thread 종료
        if (parsed_data[4] == ':q!'):
            break
        
        ######################################################
        #암호화하여 전달(server -> client)
        #암호화1(pad처리)
        padded_data = pad(decoded_data.encode(), AES.block_size)

        #암호화2(pad된 데이터를 encrypt하여 암호화)
        encrypted_data = cipher.encrypt(padded_data)
        
        #암호화된 데이터를 client로 전송
        connection.sendall(encrypted_data);
        
        sleep(1)
    
    #q를 입력받아 thread가 종료되면 connection을 끊기 전 화면에 표시할 값
    print("socket closed")
    connection.close()

#################################################################        

while True:
    #server는 client의 connect를 대기하고 있음을 안내는 interface
    print("waiting....")
    client_socket, address = server_socket.accept()
    
    #어떤 Client와 연결되었는 지 표기
    print('Connected from: ' + address[0] + ':' + str(address[1]))

    #새로운 client와 연결될 때마다 새로운 thread생성
    start_new_thread(threaded_client,(client_socket,))
    
    #새로운 thread가 추가 생성되었으므로, thread count +1처리하고 화면에 표시
    threadCount += 1
    print('Thread Number: ' + str(threadCount))
    
server_socket.close()

