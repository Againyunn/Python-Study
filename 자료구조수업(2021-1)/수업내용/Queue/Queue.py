#원형 큐 클래스 구현(index 0부터 시작)
class Queue1:
    MAX_QSIZE = 100
    def __init__(self):
        self.items=[None]*Queue1.MAX_QSIZE
        self.front=-1 #시작점
        self.rear=-1 #index번호
        self.size=0 #원소의 개수
        #front와 rear모두 -1 로 지정한 이유 : 원소가 하나씩 추가될 때마다 rear+=1이 되는데, 이때 rear은 큐의 마지막(index번호 역할), size는 원소의 개수 역할을 수행한다.
        #따라서 front와 rear모두 -1로 시작을 해야 index 번호도 0부터 시작되므로
        #만약 front와 rear모두 0으로 지정한다면, index 번호는 1부터 시작된다.

        #ADT구분:
        # front: 시작점
        # rear: 큐의 마지막(원소가 추가 될 때마다 rear+=1)
        # size: 큐의 사이즈를 측정하기 위한 변수(큐가 가득 찼을 때 새로 추가하기 위한 방법)

    def isEmpty(self): #Queue가 비어있을 때
        return self.size ==0 #size가 0일때 True 반환
    
    def enqueue(self,e): #Queue의 원소 삽입
        if self.size == len(self.items):
            print("Queue is full")
            #self.resize(2*len(self.items)) #Queue가 가득 찼을 때 기존 원소량의 2배로 늘린다는 명령어, 필요시 추가
        else:
            self.rear=(self.rear+1)%(len(self.items)) #원소가 추가될 때는 rear+=1 씩 하여 인덱스를 측정한다.
            self.items[self.rear] =e
            self.size +=1
    
    def dequeue(self): #Queue의 원소 반환후 삭제
        if self.isEmpty:
            print("Queue is empty")
        else:
            self.front = (self.front+1)%(len(self.items))
            e=self.items[self.front]
            self.size-=1
            return e

    def resize(self,cap): #Queue의 원소 크기 재조정(늘리기)
        olditmes=self.items
        self.items = [None]*cap
        walk=(self.front+1)%len(olditmes) # walk 초기값 : 새로운 원소들을 추가해서 체크해야 하므로 front+1 을 한 뒤에 기존 Queue원소들의 개수로 나누어 체크

        for k in range(self.size): #원소의 개수만큼 반환
            self.items[k] = olditmes[walk] #기존 큐에 저장되어 있던 원소들을 olditems에 담아뒀다가 새로운 큐에 복사하는 과정
            walk = (walk+1)%len(olditmes) #다음 walk 순서로 넘어가도록 지정
        
        self.front =-1
        self.rear=self.size -1

    def peek(self): #Queue의 첫번째 원소를 삭제하지 않고 반환
        return self.items[self.front]

    def size(self): #Queue의 원소 개수 반환
        return self.size
    
    def clear(self): #Queue 초기화
        if self.size==0: #Queue가 이미 비어있을 경우
            return
        
        else: #Queue에 원소가 있는 경우
            for i in range(self.size): 
                self.items[i-1] = None
            return

#원형 큐 클래스 구현(index 1부터 시작)
#원형 큐 클래스 구현(index 0부터 시작)
class Queue2:
    MAX_QSIZE = 100
    def __init__(self):
        self.items=[None]*Queue2.MAX_QSIZE
        self.front=0
        self.rear=0
        self.size=0
        #만약 front와 rear모두 0으로 지정한다면, index 번호는 1부터 시작된다.

    def isEmpty(self):
        return self.size ==0 #size가 0일때 True 반환
    
    def enqueue(self,e):
        if self.size == len(self.items):
            print("Queue is full")
            #self.resize(2*len(self.items)) #Queue가 가득 찼을 때 기존 원소량의 2배로 늘린다는 명령어
        else:
            self.rear=(self.rear+1)%(len(self.items))
            self.items[self.rear] =e
            self.size +=1
    
    def dequeue(self):
        if self.isEmpty:
            print("Queue is empty")
        else:
            self.front = (self.front+1)%(len(self.items))
            e=self.items[self.front]
            self.size-=1
            return e

    def resize(self,cap):
        olditmes=self.items
        self.items = [None]*cap
        walk=(self.front+1)%len(olditmes) # walk 초기값 : 새로운 원소들을 추가해서 체크해야 하므로 front+1 을 한 뒤에 기존 Queue원소들의 개수로 나누어 체크

        for k in range(self.size):
            self.items[k] = olditmes[walk]
            walk = (walk+1)%len(olditmes) #다음 walk 순서로 넘어가도록 지정
        
        self.front =0
        self.rear=self.size

    def peek(self): #Queue의 첫번째 원소를 삭제하지 않고 반환
        return self.items[self.front]

    def size(self): #Queue의 원소 개수 반환
        return len(self.size)
    
    def clear(self): #Queue 초기화
        if self.size==0: #Queue가 이미 비어있을 경우
            return
        
        else: #Queue에 원소가 있는 경우
            for i in range(self.size): 
                self.items[i-1] = None
            return

