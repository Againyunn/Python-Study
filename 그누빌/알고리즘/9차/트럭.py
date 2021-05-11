def solution(bridge_length, weight, truck_weights):
    bridgeQueue=[]
    second= bridge_length 
    
    for truck in truck_weights:
        while truck != 0: #i번째 트럭의 무게 확인 
            if len(bridgeQueue) == bridge_length : #다리에 트럭이 가득 찬 경우
                bridgeQueue.pop(0) 

            if (sum(bridgeQueue)+truck) <= weight:  #다리를 지나고 있는 트럭 + 새로운 트럭 <= 다리 최대 중량
                bridgeQueue.append(truck)  
                truck=0 # 입력된 트럭은 0으로 바꾸어 while 반복 탈출
                second +=1 
                
            else: 
                bridgeQueue.append(0) 
                second+=1 
    
    return second