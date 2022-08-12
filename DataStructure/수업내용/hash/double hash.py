class Dictionary:
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
        print(f'소수R : {R}')
        return R - ( key % R )
    
    def put(self, key, value):
        initialPos = self.h1(key)
        i = initialPos
        h2 = self.h2(key)
        j = 0
        print(f'h1(i) = {i}')

        while True:
            
            if self.keyList[i] == None: #keyindex에 일치하는 원소가 None인 경우:  입력받은 key와 value를 각각 리스트에 담는 작업(함수의 생성자 역할)
                self.keyList[i] = key
                self.valueList[i] = value
                self.N += 1
                print("*")
                return
            
            if self.keyList[i] == key: #key와 동일한 값의 인덱스를 찾은 경우: 해당 원소의 value값을 변경(단, 앞의 if가 작동해야만 새로운 value를 지정받는다.) 
                self.valueList[i] = value
                print("**")

                return

            j += 1
            i = (initialPos + j*h2)%self.M
            print(f'h2(i) = {i}')
            
            if self.N > self.M:
                return

    def get(self, key):
        initialPos = self.h1(key)
        i = initialPos
        h2 = self.h2(key)
        j = 0

        while self.keyList[i] != None:
            if self.keyList[i] == key:
                return self.valueList[i]
            
            j += 1
            i = (initialPos + j*h2)%self.M
        return None

    def printout(self):
        print(self.keyList)
        print(self.valueList)
        return

d=Dictionary(13)
d.put(25,'가')
d.put(37,'나')
d.put(18,'다')
d.put(55,'라')
d.put(22,'마')
d.put(35,'바')
d.put(50,'사')
d.put(63,'아')
out1=d.get(35)
out2=d.get(50)
print(out1)
print(out2)
d.printout()

