print('a부터 b까지 정수의 합을 구합니다.')
a=int(input('정수a를 입력하세요.'))
b=int(input('정수b를 입력하세요.'))

if a>b: #a를 for반복문 에서 시작하는 수로 사용할 것이기에 a가 b보다 클 경우의 조건 지정
    a,b= b,a #a가 b보다 클 경우이므로, b에 더 큰 수가 들어가도록 a와 b의 숫자를 바꿔준다.
    #a와 b를 오름차순으로 정렬

sum=0
for i in range(a,b+1): #for반복문은 for i in range(0 , n) 일 때, n-1번째까지의 연산을 구한다. 따라서 반드시 반복할 만큼의 수+1 처리를 해주어야 한다.
    sum+=i

print(f'{a}부터 {b}까지 정수의 합은 {sum}입니다.')