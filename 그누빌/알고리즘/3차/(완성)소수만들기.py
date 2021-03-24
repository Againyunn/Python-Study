def solution(nums):
    nums=list(map(int,nums)) #입력받은 수를 integer 데이터 형태로 list저장
    member=len(nums)#member= nums의 원소 개수
    
    # 1. 소수를 검색할 범위 지정
    max=0#입력받은 값 중에 최고 값이 무엇인지 측정하기 위한 변수
    for c in nums: 
        if c>max:
            max=c #members의 원소 중에 기존 max보다 큰 값이 있다면 max의 값을 해당 원소의 값으로 변환
    
    # 2. 입력받은 수의 범위에 따른 소수 선별
    pri=[]# 소수를 담은 변수
    max_num=(3*max)-3 #worst case : (max-2) + (max-1) + max 
    for A in range(2, max_num): #2부터 max_num까지 범위의 수
        for i in range(2, max_num): #max_num까지의 수 중 i로 지정된 숫자마다의 값을 대입
            if A % i ==0: #소수 판별 (가능한 이유 : i중 한번이라도 A를 나눌 수 있는 경우에는 순환을 중지하고 pri에 추가하므로 A= 4일 때 i=2만을 pri에 저장)
                pri.append(i)
                break
    
    print(pri)
    # 3. 입력받은 수 중 무작위로 3개의 수를 더 했을 때 소수인지 판별
    result=[]#result= 소수를 담을 빈 리스트
    for i in range(member): #nums의 원소 개수만큼 순환
        for j in range(i,member): # i보다 큰 원소만 순환
            for k in range(j,member):# j보다 큰 원소만 순환
                if i!=j!=k:#각 인덱스가 중복되지 않는 경우
                    n=nums[i]+nums[j]+nums[k] #n: 측정 값을 담을 변수 
            
                    if pri.count(n): # n이 소수가 맞는 지 확인 = pri에 n이 존재하는 경우
                        result.append(n) #result에 추가
    answer=len(result)# answer= result의 원소 수 
    return answer #정답 반환

nums=list(input().split())
sol=solution(nums)
print(sol)