print('1부터 n까지 정수의 합을 구합니다.')
n=int(input('n값을 입력하세요.'))

sum=0
for i in range(1,n+1):
    sum+=i
print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')

#가우스의 덧셈을 통해서도 동일한 값을 도출해낼 수 있다.
#sum=n*(n+1)/2
for i in range(0,10,2): # range(인수1, 인수2, 인수3) --> 인수1 부터 인수2까지의 수를 인수3의 간격으로 출력한다는 명령어(수열의 형태)
    print(i)