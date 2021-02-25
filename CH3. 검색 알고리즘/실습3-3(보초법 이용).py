from typing import Sequence, Any
import copy

def Sequence_search(seq: Sequence, key: Any):
    a = copy.deepcopy(seq) # list a 의 값을 복사한 뒤, key의 값을 a의 맨 뒤에 새로운 원소로서 추가
    a.append(key)

    i=0
    #c=0 검색 불가능 값이 연산되는 경우의 수 계산용
    #d=0 검색 가능 값이 연산되는 경우의 수 계산용
    while True:
        if a[i] == key:
            break
        i+=1
    if i == len(seq):
        #c+=1
        #print(c)
        return -1
    else:
        #d+=1
        #print(d)
        return i

if __name__=='__main__':
    num=int(input('원소 수를 입력하세요. : '))
    x = [None] * num

    for i in range(num):
        x[i]= int(input(f'x[{i}]: '))

    key= int(input('검색할 값을 입력하세요. :'))

    idx= Sequence_search(x, key)

    if idx == -1:
        print('검색값을 갖는 원소가 없습니다.')
    else:
        print(f'검색값은 x[{idx}]에 있습니다.')
 


        