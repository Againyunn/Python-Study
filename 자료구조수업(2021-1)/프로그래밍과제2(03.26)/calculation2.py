class calculator2:
    def __init__(self):
        self.num=0 #실제 입력 값
        self.memory=0 #가상메모리
    def setValue(self,x):
        self.num=x
    def getValue(self):
        return self.num
    def add(self,x):
        self.num+=x
    def sub(self,x):
        self.num-=x
    def mpy(self,x):
        self.num*=x
    def div(self,x):
        self.num//=x
    def mod(self,x):
        self.num%=x
    def clear(self):
        self.num=0

    def changeSum(self): #현재 값의 부호 바꾸기
        self.num=-(self.num) #기존 메모리 값에 - 부호
    def memorySave(self): #현재 값을 메모리에 넣기 
        self.memory=self.num
    def memoryRead(self): #메모리 값을 현재 값으로 넣기
        self.num=self.memory
    def memoryClear(self): #메모리 값 초기화
        self.memory=0
    def memoryAdd(self): #메모리 값에 현재 
        self.memory+=self.num
    def memorySub(self):
        self.memory-=self.num
    