print('a부터 b까지 정수의 합을 구합니다.')
a = int(input('정수a의 값을 입력하세요.'))
b = int(input('정수b의 값을 입력하세요.'))

if a >b :
    a,b=b,a

sum=0
for i in range(a,b+1):
    if i<b:
        print(f'{i} + ',end='') # print 구문에 인자로서 end=''를 넣는 이유 --> 출력할 print 내의 값을 한 줄로 연달아 출력하기 위해
        # 만약에 end 없이 print로서 값들을 출력할 경우, 한 줄씩 띄어져서 값들이 출력된다.

    else :
        print(f'{i} = ',end='')
    
    sum+=i
print(sum)

print(f'{a}부터 {b}까지 정수의 합은 {sum}입니다.')