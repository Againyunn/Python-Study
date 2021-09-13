import time, random

# code for prefixSum1
def prefixSum1(X, n):
    S=[]
    for a in range(n): #임의의 값 0을 S에 n개 입력
        S.append(0)

    for i in range(0, n):
        S[i]=0
        for j in range(0, i+1):
            S[i]+=X[j]

    #print(S) #테스트용
    return S[n-1]

# code for prefixSum2
def prefixSum2(X, n):
    S=[]
    for a in range(n): #임의의 값 0을 S에 n개 입력
        S.append(0)

    S[0]=X[0]
    for i in range(1,n):
        S[i] = S[i-1]+X[i]
    #print(S) #테스트용

    return S[n-1]

random.seed()  # random 함수 초기화
# n 입력받음
n=int(input())

# 리스트 X를 randint를 호출하여 n개의 랜덤한 숫자로 채움
X=[]
for i in range(n):
    ran=random.randint(0,n)
    X.append(ran)
    # print(f'{i}번째 계수: {X[i]}')

# prefixSum1 호출
start1=time.time()
pre1= prefixSum1(X, n)
end1=time.time()

# prefixSum2 호출
start2=time.time()
pre2= prefixSum2(X, n)
end2=time.time()

# 두 함수의 수행시간 출력
print(f'prefixSum1 : {end1-start1: .20f}')
print(f'prefixSum2 : {end2-start2: .20f}')

#두 함수의 수행결과 출력
# print(pre1) #테스트용
# print(pre2) #테스트용
