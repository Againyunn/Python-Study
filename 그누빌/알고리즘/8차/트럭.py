def solution(bridge_length, weight, truck_weights):
    bridge_length=int(bridge_length)
    print(truck_weights)
    waitingTruck=list(map(int,truck_weights)) #다리 건너기 전
    truckNum=len(truck_weights)
    #movingTruck=[] #다리를 건너는 중
    movedTruck=[] #다리 건넘
    
    runTime=0 #시간 측정 용
    
    for j in range(truckNum):
        if (waitingTruck[j]<weight) :
            if waitingTruck[j] not in movedTruck:
                try :
                    a=movedTruck.index(waitingTruck[j])
                    print(f'a: {a}')
                except ValueError:    
                    Sum=int(waitingTruck[j]) #한번에 건너갈 수 있는 트럭의 무게 합: 초기값 지정
                    runTime+=bridge_length
                    #
                    movedTruck.append(waitingTruck[j])
                    print(Sum)
                    print(f"소요시간1: {runTime}")
            
         #한번에 여러 트럭이 지나갈 수 있는 경우
        for i in range(1,truckNum):

            while(weight>=Sum):
                if(j<i) and ((waitingTruck[i]+waitingTruck[j])<=weight):
                    print(f"트럭번호{i}")
                    Sum+=waitingTruck[i]
                    plus=bridge_length
                    if Sum<=weight:
                        runTime+=plus
                    movedTruck.append(waitingTruck[i])
                    print(Sum)
                    print(f"소요시간2: {runTime}")
                break

    return runTime

bridge_length = int(input("bridge_length :" ))
weight =  int(input("weight :" ))
truck_weights = input("트럭을 입력하세요 :").split()
sol=solution(bridge_length, weight, truck_weights)
print(sol)