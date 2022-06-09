import socket

from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad

key = '!!12345678900987654321!!12345678'
iv = '1234567890123456'

cipher = AES.new(key.encode(), AES.MODE_CBC, iv.encode())
decipher = AES.new(key.encode(), AES.MODE_CBC, iv.encode())

#TCP로 통신하도록 socket설정
client_socket =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

while True:
    #화면에 출력하여 안내하는 interface
    input_data = input("SEND( type :q! to Quit) :")
    
    #숫자나 boolean등 str이외의 데이터 타입은 모두 str으로 타입 변환 후 전송해야 한다.
    num_1 = 1           
    num_2 = 2          
    char_1 ='가나다라'   #parsed_data[3]
    
    snum1 = str(num_1)   #parsed_data[1]
    snum2 = str(num_2)   #parsed_data[2]
    send_data = 'checked' + ',' + snum1 + ',' + snum2 + ','+ char_1 + ',' + input_data
    print("send : ", send_data)

    ######################################################
    #암호화하여 전달(client -> server)
    #암호화1(pad처리)
    padded_data = pad(send_data.encode(), AES.block_size)
    print("padded : ", padded_data)

    #암호화2(pad된 데이터를 encrypt하여 암호화)
    encrypted_data = cipher.encrypt(padded_data)
    print("encrypted : ", encrypted_data)
    
    #암호화된 데이터를 server로 전송
    client_socket.send(encrypted_data)

    #사용자 입력이 'q'이면 thread 종료
    if(input_data == ':q!'):
        client_socket.close()
        break
    
    ######################################################
    #전달받은 데이터 해독(server -> client)
    recv_data = client_socket.recv(4096) #최대 4096bit까지 수신가능
    
    #복호화1(decrypted)
    decrypted_data = decipher.decrypt(recv_data)

    #복호화2(decrypted 된 데이터를 unpad처리)
    unpadded_data = unpad(decrypted_data, AES.block_size)

    #디코딩(unpad된 데이터를 decoding)
    decoded_data = unpadded_data.decode()
    
    print(recv_data)
    print(decrypted_data)
    print(unpadded_data)
    print(decoded_data)
    
#client socket이 닫히고 while 무한루프 밖으로 나오면, client socket이 종료되었음을 화면에 표시
print("socket closed")
    