import socket
import winsound as sd

#알람 소리
def beepsound():
    fr = 2000    # range : 37 ~ 32767
    du = 1000     # 1000 ms ==1second
    sd.Beep(fr, du) # winsound.Beep(frequency, duration)

#실수 값인 지 식별
def isNumber(s):
  try:
    float(s)
    return True
  except ValueError:
    return False

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
print("<<온도 측정 장치>>")
region = input("기온 측정 지역을 입력해주세요: ")

print("\t\t<사용방법>\n온도 입력: 현재 기온을 '숫자'로만 입력해주세요.\n지역 변경 방법: change를 입력해주세요.\n종료 방법: exit를 입력해주세요.")
while True:
    #화면에 인터페이스 출력
    temperature = input(f"\n[{region}]온도 입력\n>>>")

    #입력 값 예외 처리
    if isNumber(temperature) == False: #숫자 값인 경우
        if temperature == "change":
            region = input("기온 측정 지역을 새롭게 입력해주세요: ")
            continue
        elif temperature == "exit":
            pass
        else:
            print("온도 값으로 숫자를 입력해주세요.")
            continue

    #전송할 데이터
    data = f'{region},{temperature}'

    network_success = True

    #사용자로부터 입력받은 값을  server로 전달
    try:
        client_socket.send(data.encode())
    except:
        network_success = False
    
    #server와 통신 상태 확인
    try:
        data = client_socket.recv(port).decode() #.recv 반환 값: 비트열 데이터 -> .decode: 문자열 데이터
        if network_success == True and (data == 'T' or data == "R"):
            if data == "R":
                beepsound()
                print("Warning[온도 모니터링 장치]: 기온을 다시 한번 측정해주세요!!!")
                continue

            print('[온도 모니터링 장치] 통신 상태가 양호합니다.')
    except:
        print("Error: 온도 모니터링 장치와의 통신에 문제가 발생했습니다.")

    #입력한 값이 q나 Q면 종료 
    if temperature == 'exit':
        client_socket.close()
        break

print("온도 측정 장치를 종료합니다.")