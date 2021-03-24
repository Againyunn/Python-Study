print('a부터 b까지 정수의 합을 구합니다.')
a=int(input('정수a의 값을 입력하세요.'))
b=int(input('정수b의 값을 입력하세요.'))

if a>b:
    a,b=b,a

sum=0
for i in range(a,b):
    print(f'{i} + ',end='')
    sum+=i
print(f'{b} = ',end='') #실습 1-10에서는 for반복문 내의 if구문이 else의 조건을 충족할 때까지 반복되는 비효율 발생 --> 이를 개선
sum+=b                  # for안에 b-1까지만 연산하고, b의 조건일 때는 sum +b를 직접 수행하여 시스템의 효율을 강화
print(sum)