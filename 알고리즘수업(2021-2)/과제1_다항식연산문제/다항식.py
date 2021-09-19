import time, random

# code for O(n^2)-time function
def evaluate_n2(A, x):
    mul=[1] #차수별 x항 기록
    m=1 #매 연산 시 x항
    answer=0 #결과값 연산
    num =len(A) #차수 A 개수
    for i in range(num):
        for j in range(num-1):
            m*=x
            mul.append(m)
        temp=mul[i]*A[i]
        answer+=temp
    return answer

# code for O(n)-time function
def evaluate_n(A, x):
    mul=[1] #차수별 x항 기록
    m=1 #매 연산 시 x항
    answer=0 #결과값 연산
    num=len(A) #차수 A 개수
    for i in range(num-1):
        m*=x
        mul.append(m)
    for j in range(num):
        temp=mul[j]*A[j]
        answer+=temp
    return answer

random.seed()  # random 함수 초기화
# n 입력받음
n=int(input())
# 리스트 A를 randint를 호출하여 n개의 랜덤한 숫자로 채움
A=[]
for i in range(n):
    ran=random.randint(-1000,1000)
    A.append(ran)
    #각 계수 값 확인 -> 다항식 연산 되는 지 여부 확인용
    # print(f'항수{i}차: {ran}') 

#x입력받기(미지수 입력 받기)
x=int(input())

# evaluate_n2 호출 & 수행시간 기록
start_n2=time.process_time()
n2=evaluate_n2(A, x)
end_n2=time.process_time()

# evaluate_n 호출 & 수행시간 기록
start_n=time.process_time()
n=evaluate_n(A, x)
end_n=time.process_time()

# 두 함수의 수행시간 출력
print(f'n2수행시간 : {end_n2-start_n2: .9f}')
print(f'n수행시간  : {end_n-start_n: .20f}')

#결과값 일치 테스트(다항식 연산 가능 여부)
# print(n2)
# print(n)