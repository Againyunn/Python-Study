class Hash:
    def __init__(self, size): #생성자
        self.M = size #Hash Table의 원소 개수를 담기 위한 변수M
        self.keyList = [None] * size #keyList : key 를 담기 위한 변수
        self.valueList = [None] * size #valueList : value 를 담기 위한 변수
        self.N = 0 #Hash Table에 추가된 원소의 수를 기록할 변수

    def h1(self, key): #기본 해시 함수
        return key % self.M 
    
    def h2(self, key): #충돌 해시 함수
        R=0 #M보다 작은 가장 큰 소수를 담을 변수
        for n in range(2, self.M): #M보다 작은 수 중 최대 크기 소수 판별
            for i in range(2, n):
                if n % i == 0:
                    break
            else:
                R = n #n의 값이 커짐에 따라 R에 업데이트(R이  점점커짐)
        return R - ( key % R ) 
    
    def put(self, key, value): #리스트에 값 추가
        initialPos = self.h1(key) #최초 해시 값
        i = initialPos #변화할 해시 값(key)
        h2 = self.h2(key) #충돌 시 2차 해시 값
        j = 0 #연산 횟수를 기록하기 위한 변수 j


        while True:
            
            if self.keyList[i] == None: #keyindex에 일치하는 원소가 None인 경우:  입력받은 key와 value를 각각 리스트에 담는 작업(함수의 생성자 역할)
                self.keyList[i] = key
                self.valueList[i] = value
                self.N += 1
                return
            
            if self.keyList[i] == key: #key와 동일한 값의 인덱스를 찾은 경우: 해당 원소의 value값을 변경(단, 앞의 if가 작동해야만 새로운 value를 지정받는다.) 
                if self.valueList[i] != value:
                    self.valueList[i] = value
                    return
                else: #key가 동일한데, value가 다른 경우
                    error1 = 'error1'
                    return error1

            j += 1
            i = (initialPos + j*h2)%self.M #충돌에 따라 새로운 해시값을 i에 부여

            if self.N > self.M: #"입력 받은 원소 = 리스트의 길이" 경우 반환
                return
    
    def change(self, key, value): #리스트에 있는 원소 값 바꾸기
        initialPos = self.h1(key) #최초 해시 값
        i = initialPos #변화할 해시 값(key)
        h2 = self.h2(key) #충돌 시 2차 해시 값
        j = 0 #연산 횟수를 기록하기 위한 변수 j

        while True:
            if self.get(key) == 'error2': #입력 받은 데이터(key)와 일치하는 원소가 없는 경우(error2)
                error2 = 'error2'
                return error2
            
            if self.keyList[i] == None: #keyindex에 일치하는 원소가 None인 경우:  입력받은 key와 value를 각각 리스트에 담는 작업(함수의 생성자 역할)
                self.keyList[i] = key
                self.valueList[i] = value
                self.N += 1
                return
            
            if self.keyList[i] == key: #key와 동일한 값의 인덱스를 찾은 경우: 해당 원소의 value값을 변경(단, 앞의 if가 작동해야만 새로운 value를 지정받는다.) 
                self.valueList[i] = value
                return

            j += 1
            i = (initialPos + j*h2)%self.M #충돌에 따라 새로운 해시값을 i에 부여

            if self.N > self.M: #"입력 받은 원소 = 리스트의 길이" 경우 반환
                return

    def get(self, key):
        initialPos = self.h1(key)  #최초 해시 값
        i = initialPos #변화할 해시 값(key)
        h2 = self.h2(key) #충돌 시 2차 해시 값
        j = 0 #연산 횟수를 기록하기 위한 변수 j
        error2 = 'error2'

        while self.keyList[i] != None: #순차적으로 변경되는 모든 key의 값들 중 최후 값과 일치하는 키의 인덱스가 비어있는 경우(찾는 key와 일치하는 원소가 없는 경우)
            if self.keyList[i] == key:
                return self.valueList[i]
            
            j += 1
            i = (initialPos + j*h2)%self.M
        return error2 #조회 실패

dic=Hash(997)#임의의 size지정 -> 1000이하의 정수 중 최대 소수를 size로 지정

# i[0] : Key, i[1] : word value
while True:
    command = input().split()
    if len(command) > 1:
        temp = command[1]
        key = 0
        for j in range(len(temp)):#key 형태 변환(str >> int) 
            key += ord(temp[j]) #아스키 코드로 변환하여 int형의 key값 생성

    if command[0] == '단어삽입' : #단어 삽입
        insert = dic.put(key, command[2])
        if insert == 'error1':
            print('error1')

    if command[0] =='단어뜻수정': #단어 수정
        rewrite = dic.change(key, command[2])
        if rewrite == 'error2':
            print('error2')

    if command[0] == '단어검색': #단어 조회 후 출력
        output = dic.get(key)
        print(output)

    if command[0] == '종료':
        break

    else:
        pass







