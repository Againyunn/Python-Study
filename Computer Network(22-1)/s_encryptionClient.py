import socket

from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad

key = '!!12345678900987654321!!12345678'
iv = '1234567890123456'
bufferSize = 1024



#TCP로 통신하도록 socket설정
client_socket =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

while True:
    #새로운 thread 생성할 때마다 AES의 값을 초기화하는 작업 필요(안그러면 충돌발생하여 추가 thread생성 시 오류 발생)
    cipher = AES.new(key.encode(), AES.MODE_CBC, iv.encode())
    decipher = AES.new(key.encode(), AES.MODE_CBC, iv.encode())

    #화면에 출력하여 안내하는 interface
    input_data = input("SEND( type :q! to Quit) :")
    
    print("send : ", input_data)

    ######################################################
    #암호화하여 전달(client -> server)
    #암호화1(pad처리)
    padded_data = pad(input_data.encode(), AES.block_size)

    #암호화2(pad된 데이터를 encrypt하여 암호화)
    encrypted_data = cipher.encrypt(padded_data)
    
    #암호화된 데이터를 server로 전송
    client_socket.send(encrypted_data)

    #사용자 입력이 'q'이면 thread 종료
    if(input_data == ':q!'):
        client_socket.close()
        break
    
    ######################################################
    #전달받은 데이터 해독(server -> client)
    recv_data = client_socket.recv(bufferSize) #최대 4096bit까지 수신가능
    
    #복호화1(decrypted)
    decrypted_data = decipher.decrypt(recv_data)

    #복호화2(decrypted 된 데이터를 unpad처리)
    unpadded_data = unpad(decrypted_data, AES.block_size)

    #디코딩(unpad된 데이터를 decoding)
    decoded_data = unpadded_data.decode()
    
    print(decoded_data)
    
#client socket이 닫히고 while 무한루프 밖으로 나오면, client socket이 종료되었음을 화면에 표시
print("socket closed")
    