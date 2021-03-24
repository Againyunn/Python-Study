from typing import Any, Sequence

def bin_search(a: Sequence, key: Any )-> int:
    pl= 0 #pl : 맨 앞 값
    pr= len(a)-1 #pr : 맨 뒤 값
    #key : 검색값

    while True:
        pc = (pl+pr)//2 #pc : 중앙 원소 값
        if a[pc] == key:  
            return pc
        elif a[pc] < key:  #중간 값보다 검색 값이 클 때
            pl = pc +1  
        else: #a[pc] > key 검색 값보다 중간 값이 클 때
            pr = pc-1
        if pl>pr: # 맨 앞의 값이 맨 뒤 값보다 클 때
            return -1 # 검색 실패
            break
        
if __name__=='__main__' :
    num = int(input('원소 수를 입력하세요. : '))
    x = [None] * num #원소 수에 맞게 임의의 list 생성

    print('배열 데이터를 오름차순으로 입력하세요. : ')

    x[0] = int(input('x[0]: '))

    for i in range(1, num):
        while True:
            x[i] = int(input(f'x[{i}]: '))
            if x[i]>=x[i-1]: #오름차순대로 입력이 안될 경우
                break
            print('오름차순대로 다시 입력하세요.')
    
    key = int(input('검색할 값을 입력하세요. : '))

    idx = bin_search(x, key)

    if idx == -1 :
        print('검색 값을 갖는 원소가 없습니다.(검색 실패)')
    else:
        print(f'검색 값은 x[{idx}]에 있습니다.(검색 성공)')
