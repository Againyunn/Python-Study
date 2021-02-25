from typing import Any, MutableSequence
def reverse_array(a: MutableSequence) -> None: #역순으로 배열을 바꾸는 함수 선언
    n = len(a) #객체 a의 원소 갯수를 의미하는 a 
    for i in range(n //2):
        a[i], a[n-i-1] = a[n-i-1], a[i] # i가 0부터~n-1까지의 값이므로 시작번호 == a[i] , 끝번호 == a[n-i-1] 이 된다.

if __name__=='__main__':
    print('배열 원소를 역순으로 정렬합니다.')
    nx = int(input('원소 수를 입력하세요.'))
    x = [None] * nx 

    for i in range(nx):
        x[i] = int(input(f'x[{i}]값을 입력하세요.:'))

    reverse_array(x)

    print('배열 원소를 역순으로 정렬했습니다.') 
    for i in range(nx):
        print(f'x[{i}]={x[i]}')

