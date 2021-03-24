print('*를 출력합니다.')
n=int(input('몇 개를 출력할까요?: '))
w=int(input('몇 개를 간격으로 줄바꿈할까요?: '))

for i in range(1,n+1):
    print('*',end='')
    if i % w == 0:
        print()
