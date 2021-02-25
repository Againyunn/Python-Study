counter = 0         #연산의 횟수
ptr = 0             #소수의 갯수
prime = [None] * 500#소수 자체를 리스트 prime 안에 저장 -> 임의의 방 500개를 생성

prime[ptr]= 2
ptr+=1

for n in range(3,1001,2): #홀수만 대상으로 연산 진행 -> 어차피 짝수는 모두 2로 나눌 수 있기때문
    for i in range(ptr):
        counter +=1
        if n % prime[i] == 0:
            break

    else:
        prime[ptr] = n
        ptr+=1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         


for i in range(ptr): # ptr(소수의 갯수) 와 prime(소수 리스트) 배열을 조합하여 값 출력
        print(prime[i]) 
print(f'나눗셈을 실행한 횟수 : {counter}')