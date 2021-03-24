from typing import Sequence, Any

def bin_search(a: Sequence, key : Any) -> int:
    pl = 0 # 맨 앞의 값
    pr = len(a)-1 # 맨 뒤의 값
    #key : 검색 값

    print('  |', end=' ')
    for i in range(len(a)):
        print(f'{i : 4}', end=' ')
    print()
    print('---+' + (4*len(a) +2 )* '-')

    while True:
        pc= (pl+pr)//2

        print('  |', end= ' ')
        if pl != pc:
            print((pl * 4 + 1) * ' ' + '<-' + ((pc-pl)*4) * ' '+'+',end=' ')
        else:
            print((pc* 4 + 1)* ' '+'<+',end= ' ')
        if pc != pr:
            print(((pr-pc)*4-2)*' ' +'->')
        else:
            print('->')
        print(f'{pc:3}|', end=' ')
        
        for i in range(len(a)):
            print(f'{a[i]:4}', end=' ')
        print('\n  |')
       

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