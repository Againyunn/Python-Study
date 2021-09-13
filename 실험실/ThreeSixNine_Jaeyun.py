num=int(input())
#num이 10이상인경우, 3의 배수 뿐만 아니라 끝자리가 3,6,9가 들어갈 수 있으므로 10이하, 10초과 두가지의 경우로 분리하여 연산

for i in range(1,num+1):
    if i<=10: #10을 포함하여 1의 자리인경우
        if i%3==0: #3의 배수
            print(f'{0}',end=' ')
        else: #그외
            print(f'{i}',end=' ')
    else: #10<num<=100인경우
        temp = i % 10
        if i%3==0:#3의 배수
            print(f'{0}',end=' ')
        elif temp%3==0: #끝자리가 3,6,9인 경우
            print(f'{0}',end=' ')
        else: #그외
            print(f'{i}',end=' ')

