counter = 0

for n in range(2, 1001): #2부터 1000까지 범위의 수
    for i in range(2, n): #n까지의 수 중 i로 지정된 숫자마다의 값을 대입
        counter+= 1 #연산이 시작될 때 마다 counter의 숫자 상승
        if n % i ==0: #만약 n / i 했을 때 0의 값이 나온다면 소수임이 맞으므로 if의 순환을 멈춘다.
            break
    else:       #if 문이 실행되지 break 처리 되어 실행되지 않을 경우, 다음 줄의 코드가 실행되는 원리 이용
        print(n) # n/i 의 값이 0이 아닌 경우이므로 해당 숫자(n)을 출력
print(f'나눗셈을 실행한 횟수: {counter}')
