def solution(nums):
    nums=list(map(int,nums))
    member=len(nums)#member= nums의 원소 개수

    pri=[]# 소수를 담은 변수
    for A in range(2, 2998): ##2부터 1000까지 범위의 수를 무작위로 3개 더했을 때 worst case = '998'+'999'+'1000' ='2997'임을 감안
        for i in range(2, 2998): #n까지의 수 중 i로 지정된 숫자마다의 값을 대입
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
