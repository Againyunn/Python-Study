def solution(nums):
    nums=list(map(int,nums))
    member=len(nums)#member= nums의 원소 개수
    
    max=0#입력받은 값 중에 최고 값이 무엇인지 측정하기 위한 변수
    for c in nums:
        if c>max:
            max=c #members의 원소 중에 기존 max보다 큰 값이 있다면 max의 값을 해당 원소의 값으로 변환
    
    pri=[]# 소수를 담은 변수
    max_num=(3*max)-3 #worst case : (max-2) + (max-1) + max 
    for A in range(2, max_num): ##2부터 max_num까지 범위의 수를 무작위로 3개 더한 경우
        for i in range(2, max_num): #n까지의 수 중 i로 지정된 숫자마다의 값을 대입
            if A % i ==0: #만약 A / i 했을 때 0의 값이 나온다면 소수임이 맞으므로 if의 순환 정지
                pri.append(i)
                break

    result=[]#result= 소수를 담을 빈 리스트
    for i in range(member):
        for j in range(i,member): # i보다 큰 원소값만 순환
            for k in range(j,member):# j보다 큰 원소값만 순환
                if i!=j!=k:#각 인덱스가 중복되지 않는 경우
                    n=nums[i]+nums[j]+nums[k]#n: 측정 값을 담을 변수 
                    if pri.count(n): #pri에 n이 존재하는 경우
                        result.append(n)
    answer=len(result)# answer= result의 원소 수
    return answer
