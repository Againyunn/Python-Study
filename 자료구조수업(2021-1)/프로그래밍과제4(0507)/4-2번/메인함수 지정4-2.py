# 다리 길이 w = 한번에 다리에 올라갈 수 있는 트럭의 수 w
# 트럭은 한번에 1만큼 이동가능
# 다리에 올라간 트럭들의 무게 <= 다리의 최대하중 L
class bridgeQueue:
    def __init__(self, bridgeSize, bridgeWeight):
        self.items=[None]*bridgeSize
        self.bridgeWeight=bridgeWeight
        self.front=-1 #시작점
        self.rear=-1 #index번호
        self.size=0 #원소의 개수
        
    def isEmpty(self): #Queue가 비어있을 때
        return self.size ==0 #size가 0일때 True 반환
    
    def enqueue(self,e): #Queue의 원소 삽입
        #if self.size == len(self.items):
        #    return False #False 반환 시 더이상 트럭이 들어올 수 없다.
        
        if self.bridgeWeight== weightSize(): #더이상 다리에 트럭이 추가될 수 없는 경우
            return False

        elif self.bridgeWeight < e: #트럭이 다리보다 무거운 경우(진입 불가)
            return False

        else:
            self.rear=(self.rear+1)%(len(self.items)) #원소가 추가될 때는 rear+=1 씩 하여 인덱스를 측정한다.
            self.items[self.rear] =e
            self.size +=1
    
    def dequeue(self): #Queue의 원소 반환후 삭제
        if self.isEmpty:
            return False #False 반환 시 비어있다고 처리 필요
        else:
            self.front = (self.front+1)%(len(self.items))
            e=self.items[self.front]  #다 통과한 트럭
            self.itmes[self.front]=None #이 부분이 누락된 것 같아 추가함(04.28)
            self.size-=1
            
            runtime=0
            if size()==0: #1대의 트럭만 이동한 경우(dequeue의 대상)
                runtime=self.bridgeWeight
            if size()>0:
                runtime=self.bridgeWeight-size()
            return runtime

    def weightSize(self): #현재 다리를 건너고 있는 트럭들의 무게
        itemsNum=self.rear-self.front
        weight=0
        for i in range(itemsNum):
            weight+=self.items[i%len(self.items)]
        return weight

    def size(self): #Queue의 원소 개수 반환
        answer = int(self.size)
        return self.size
    
    def clear(self): #Queue 초기화
        if self.size==0: #Queue가 이미 비어있을 경우
            return
        
        else: #Queue에 원소가 있는 경우
            for i in range(self.size): 
                self.items[i-1] = None
            return

def truckNum(self, truckWeight, bridgeSize, bridgeWeight):
    B=bridgeQueue(bridgeSize)
    allRuntime=0
    truckWeight=truckWeight
    truckNum = len(truckWeight)
    for i in range(truckNum):
        if (truckWeight[i] <= bridgeWeight) and (truckWeight[i]+B.weightSize()<=bridgeWeight): #새로운 트럭도 기존에 이동중인 트럭과 함께 이동이 가능할 때
            B.enqueue(truckWeight[i])
        if (truckWeight[i] <= bridgeWeight) and (truckWeight[i]+B.weightSize()>bridgeWeight):  #새로운 트럭이 기존에 이동중인 트럭과 동시 이동이 불가할 떄
            if B.dequeue()!=False:
                allRuntime+=B.dequeue()
    print(allRuntime)
            
i=input().split()
information=list(map(int,i))
t=input().split()
trucks=list(map(int,t))
bridgeSize=information[1]
bridgeWeight=information[2]
truckNum(trucks,bridgeSize,bridgeWeight)
