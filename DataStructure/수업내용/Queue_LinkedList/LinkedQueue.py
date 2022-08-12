class Node:
    def __init__(self, element):
        self.data=element
        self.link=None

class LinkedQueue:
    def __init__(self):
        self.front=self.rear=None #front와 rear 를 구분하여 front는 head의 기능을 수행하고 rear은 그외 Node의 인덱스를 나타낸다.
    
    def isEmpty(self):
        return self.front==None
    
    def enqueue(self, e):
        newNode=Node(e)
        if self.front==None:
            self.front=newNode
            self.rear=newNode
        else:
            self.rear.link=newNode
            self.rear=newNode

    def deQueue(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        else:
            e=self.front.data #맨 앞의 Node값을 가져온다.
            self.front = self.front.link #기존의 2번째 Node의 link를 첫번째 Node(front)로 지정
            if self.front== None: #기존에 Node가 1개여서, 2번째 Node가 없는 경우
                self.rear=None #front와 rear로 나누어 데이터를 입력하였기 때문에 rear도 None으로 초기화 해주어야 Node에 잔존 값이 없다.
            return e

