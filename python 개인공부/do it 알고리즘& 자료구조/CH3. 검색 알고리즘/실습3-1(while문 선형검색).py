from typing import Any, Sequence

def Sequence_search(a: Sequence, key: Any) -> int:
    i = 0

    while True:
        if i == len(a):
            return -1
        if a[i] == key:
            return i #검색에 성공한 배열의 인덱스를 반환
        i+=1


if __name__ == '__main__' :
    num = int(input('원소 수를 입력하세요. : '))
    x = [None] * num

    for i in range(num):
        x[i]=int(input(f'x[{i}] ='))
    
    key = int(input('검색 할 값을 입력하세요.'))

    idx = Sequence_search(x, key)
    if idx>=0:
        result = x[idx]
    
    if idx == -1:
        print('\n검색값과 일치하는 원소가 없습니다.')
    else:
        print(f'\n검색값은 x[{idx}]에 있습니다.')
        print(f'검색값은 {result}입니다.')