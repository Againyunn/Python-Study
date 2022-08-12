# 다리 길이 w = 한번에 다리에 올라갈 수 있는 트럭의 수 w
# 트럭은 한번에 1만큼 이동가능
# 다리에 올라간 트럭들의 무게 <= 다리의 최대하중 L

# 우선 단순히 무게만 주어지는 트럭의 정보에 한 가지를 더 포함시켰다. 
# 다리에 올라간 순간 다리에 오른 시간을 현재 시간으로 한다. 
# 그리고 올라간 시간에 다리 길이를 더한 값보다 지금 시간이 크다면 그 트럭을 다리에서 제거했다. 
# 이것을 다리와 대기 리스트에 트럭이 없을 때 까지 반복한다.

class bridgeQueue:
    def __init__(self, bridgeSize, bridgeWeight):
        self.items=[]
        self.bridgeWeight=bridgeWeight
        self.bridgeSize= bridgeSize
        self.size=0 #원소의 개수
        
    def isEmpty(self): #Queue가 비어있을 때
        return self.size ==0 #size가 0일때 True 반환
    
    def enqueue(self,e): #Queue의 원소 삽입
        self.items.append(e)
        self.size +=1
    
    def dequeue(self): #Queue의 원소 반환후 삭제
        if self.isEmpty():
            return 0 #-1 반환 시 비어있다고 처리 필요
        else:
            e=self.items[0]  #다 통과한 트럭
            del(self.items[0]) #이 부분이 누락된 것 같아 추가함(04.28)
            self.size-=1
            return 

    def weightSize(self): #현재 다리를 건너고 있는 트럭들의 무게
        Weight=0
        for i in range(len(self.items)):
            Weight+=self.items[i]
        return Weight

    def elementsNum(self): #Queue의 원소 개수 반환
        answer = int(self.size)
        return self.size
    
    def clear(self): #Queue 초기화
        if self.size==0: #Queue가 이미 비어있을 경우
            return
        
        else: #Queue에 원소가 있는 경우
            self.items=[]
            return
    
    def peek(self): #Queue의 첫번째 원소를 삭제하지 않고 반환
        return self.items[self.front+1]
    

i=input().split()
information=list(map(int,i))
t=input().split()
truckWeight=list(map(int,t))
bridgeSize=information[1]
bridgeWeight=information[2]

B=bridgeQueue(bridgeSize,bridgeWeight)
second=0

for trcuk in truckWeight:

    while truck != 0: #i번째 트럭의 무게 확인 
        if B.elementsNum() == bridgeSize : #다리에 트럭이 가득 찬 경우
            B.dequeue()  # -> 트럭 빼기

        if (B.weightSize()+truck) <= bridgeWeight:  #다리를 지나고 있는 트럭 + 새로운 트럭 <= 다리 최대 중량
            B.enqueue(truck) # -> 새로운 트럭 추가
            truck=0 # 입력된 트럭은 0으로 바꾸어 while 반복 탈출
            second +=1 # 진입하는 1초 추가
        else: #다리가 비어있는 경우 (트럭이 빠져나오는 시간)
            B.enqueue(0) #임의 값 0입력
            second+=1 # 트럭이 빠져나오는 1초 추가

second= second + bridgeSize #트럭이 다리를 지나는 시간 추가(트럭들이 중복으로 진입, 빠져나가는 시간은 고려했으므로 다리 자체를 지나는 시간 기록)
print(second)
            




