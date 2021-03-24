print('*를 출력합니다.')
n=int(input('*를 몇 개 출력할까요? : '))
w=int(input('몇 개를 간격으로 줄바꿈할까요? : '))

for _ in range(n//w): #최종 반복할 줄의 수
    print('*'*w)      #각 반복할 줄의 수에 배정될 *의 간격수


if n%w>0:
    t = int(n%w)
    print('*'*t)  #반복을 끝내고 마지막 줄에 배열될 *의 수