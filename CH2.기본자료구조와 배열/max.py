##주의사항 : 실습 2-2.py 를 향후 사용할 실습 2-# 파일 내의 max_of 함수 호출을 위해 max.py라는 임의의 파일명으로 저장함.##

from typing import Any , Sequence


def max_of(a: Sequence) -> Any:
    maxium=a[0]
    
    for i in range(1, len(a)):
        if a[i]>maxium:
            maxium=a[i]
    return maxium
    
if __name__=='__main__':
    print('배열의 최댓값을 구합니다.')
    num=int(input('원소 수를 입력하세요.'))
    x = [None] * num

    for i in range(num):
        x[i]= int(input(f'x[{i}]값을 입력하세요.'))

    print(f'최댓값은 {max_of(x)} 입니다.')

