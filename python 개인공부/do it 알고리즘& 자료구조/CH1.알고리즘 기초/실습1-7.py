print('1부터 n까지 정수의 합 구하기')
n=int(input('숫자를 입력하세요'))

sum=0
i=1
while i<=n:
    sum+=i #sum=sum+i
    i+=1 #i=i+1
print(f'1부터{n}까지의 합은 {sum}입니다.')
print(f'i의 값은 {i}입니다.') #i는 n을 초과해야 한다.