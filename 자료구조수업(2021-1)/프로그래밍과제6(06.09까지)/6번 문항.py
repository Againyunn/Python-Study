class Hash:
    def __init__(self, size): #생성자
        self.M = size
        self.keyList = [None] * size
        self.valueList = [None] * size
        self.N = 0

    def h1(self, key): #기본 해시 함수
        return key % self.M
    
    def h2(self, key): #충돌 해시 함수
        R=0 #M보다 작은 가장 큰 소수를 담을 변수
        for n in range(2, self.M): #소수 판별 코드
            for i in range(2, n):
                if n % i == 0:
                    break
            else:
                R = n #n의 값이 커짐에 따라 R에 업데이트
        return R - ( key % R )
    
    def put(self, key, value):
        initialPos = self.h1(key)
        i = initialPos
        h2 = self.h2(key)
        j = 0


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
            i = (initialPos + j*h2)%self.M

            if self.N > self.M:
                return
    
    def change(self, key, value):
        initialPos = self.h1(key)
        i = initialPos
        h2 = self.h2(key)
        j = 0


        while True:
            if self.get(key) == 'error2':
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
            i = (initialPos + j*h2)%self.M

            if self.N > self.M:

                return

    def search(self, key): #key는 다른데, value가 동일한 원소를 조회하기 위한 함수
        fine = -1
        for i in range(len(self.keyList)):
            if self.keyList[i] == key:
                find = i
                return find
        return fine

    def get(self, key):
        initialPos = self.h1(key)
        i = initialPos
        h2 = self.h2(key)
        j = 0
        error2 = 'error2'

        while self.keyList[i] != None:
            if self.keyList[i] == key:
                return self.valueList[i]
            
            j += 1
            i = (initialPos + j*h2)%self.M
        return error2 #조회 실패

    def printout(self):
        print(self.keyList)
        print(self.valueList)
        return

dic=Hash(997)

# i[0] : Key, i[1] : word value
while True:
    command = input().split()
    if len(command) > 1:
        temp = command[1]
        key = 0
        for j in range(len(temp)):#key 형태 변환(str >> int)
            key += ord(temp[j])

    if command[0] == 'I' : #단어 삽입
        insert = dic.put(key, command[2])
        if insert == 'error1':
            print('error1')

    if command[0] =='C': #단어 수정
        rewrite = dic.change(key, command[2])
        if rewrite == 'error2':
            print('error2')

    if command[0] == 'S': #단어 조회 후 출력
        output = dic.get(key)
        print(output)

    if command[0] == 'Q':
        break

    else:
        pass







