print('1부터 n까지 정수의 합을 구합니다.')

while True:   #반복문 안의 값이 참일 때까지 실행하라는 의미
    n = int(input('n값을 입력하세요: '))
    if n >0: 
        break  # 입력받은 int n이 양수일 경우 반복을 참의 조건을 만족하여 반복을 종료한다는 의미


sum=0
for i in range(1,n+1):
    sum+=i
    i+=1

print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')