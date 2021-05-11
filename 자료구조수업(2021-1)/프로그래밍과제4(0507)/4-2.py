# 다리 길이 w = 한번에 다리에 올라갈 수 있는 트럭의 수 w
# 트럭은 한번에 1만큼 이동가능
# 다리에 올라간 트럭들의 무게 <= 다리의 최대하중 L
# 트럭의 이동 시간 second

class bridgeQueue:
    def __init__(self):
        self.items=[]
        self.size=0 #원소의 개수
    
    def enqueue(self,e): #Queue의 원소 삽입
        self.items.append(e)
        self.size +=1
    
    def dequeue(self): #Queue의 원소 반환후 삭제
        if self.items==[]:
            return 
        else:
            self.items.pop(0)
            self.size-=1
            return 

    def weightSize(self): #현재 다리를 건너고 있는 트럭들의 무게
        Weight=0
        for i in self.items:
            Weight+=i
        return Weight

    def elementsNum(self): #Queue의 원소 개수 반환
        return self.size

def solution(bridge_length, weight, truck_weights):
    B=bridgeQueue()
    second= bridge_length 
    
    for truck in truck_weights:
        while truck != 0: #i번째 트럭의 무게 확인 
            if B.elementsNum() == bridge_length : #다리에 트럭이 가득 찬 경우
                B.dequeue()  

            if (B.weightSize()+truck) <= weight:  #다리를 지나고 있는 트럭 + 새로운 트럭 <= 다리 최대 중량
                B.enqueue(truck) 
                truck=0 # 입력된 트럭은 0으로 바꾸어 while 반복 탈출
                second +=1 
                
            else: 
                B.enqueue(0) 
                second+=1 
    
    return second


