import datetime
import socket
from _thread import *
import winsound as sd

#알람 소리
def beepsound():
    fr = 2000    # range : 37 ~ 32767
    du = 1000     # 1000 ms ==1second
    sd.Beep(fr, du) # winsound.Beep(frequency, duration)

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

#알람 발생 조건
print("<<온도 모니터링 장치>>")
print("\t\t<사용방법>\n온도 측정 장치가 연결되면 온도 측정이 시작됩니다.\n본 기기는 이상기후 측정을 위한 장비로, -20 ~ 37C를 정상기온으로 인식합니다.\n또한 직전 측정보다 5C이상의 변화가 측정되면 이상기온으로 인식합니다.\n해당 정상기온을 넘어가는 기온은 이상기후로 인식하여 알람이 발생합니다.\n")

#client의 connect 요청 대기
print('온도 측정 장치와의 연결을 대기하고 있습니다...')
server_socket.listen(5)

#client가 connect하면 작동할 client와 통신할 코드
def threaded_client(connection):

    #server와 연결되었음을  client에 전달
    #connection.send(str.encode('Welcome to server'))

    #과거의 기온 이력
    past_temperature = None

    while True:
        #재 측정 요청
        recheck = False

        #client로부터 전달된 값 받기
        data = connection.recv(bufferSize).decode()

        parsed_data = data.split(',')

        region = parsed_data[0]
        temperature = parsed_data[1]

        if temperature=='exit':
            break
        
        else:
            date = datetime.datetime.now()
            #기존의 기온 이력 여부 확인
            if past_temperature == None: #최초 기록인 경우
                print(f'[{date}] 온도 측정 장치({region}): {temperature}C')
                past_temperature = float(temperature) #현재의 기온 기록을 저장하여 다음 기록 비교에 활용

            else:#기존의 기록이 있는 경우
                difference = float(temperature) - past_temperature #이전 기록과 비교
                
                if difference > 0:
                    difference = '+'+str(difference)

                print(f'[{date}] 온도 측정 장치({region}): {temperature}C [직전과 비교]: {difference}C')

                if abs(float(difference)) > 5:
                    beepsound()
                    print("Warning: 이상 기온이 감지되었습니다!!!\n\t현재의 이상 기온은 기록하지 않습니다.\n\t재측정해주세요.")
                    
                    recheck = True

            #이상 기온 측정    
            if float(temperature) < -20 or float(temperature) > 37:
                beepsound()
                print("Warning: 이상 기온이 감지되었습니다!!!\n\t정상기온의 범위를 초과했습니다.\n\t재측정해주세요.")
                recheck = True
            
         
        #client로부터 전달받은 값을  client에 다시 전달
        if recheck: 
            connection.send('R'.encode())
        else:#재측정x일 때만 기록 업데이트
            past_temperature = float(temperature) #현재의 기온 기록을 저장하여 다음 기록 비교에 활용
            connection.send('T'.encode())
    
    print(f'온도 측정 장치({region}) 연결 해제')
    connection.close()

#코드 본문
while True:
    #client가 connect요청을 하면 연결을 수락하며, client_socket과 client_address 받아서 변수에 저장하기
    client_socket, address = server_socket.accept()

    print('\n연결 요청한 온도 측정 장치: '+ address[0] + ':' + str(address[1]))

    #연결된 client별로 thread생성하여 동작
    start_new_thread(threaded_client,(client_socket,))

    threadCount += 1
    print('연결된 온도 측정 장치 수: '+str(threadCount)+'\n')

server_socket.close()

