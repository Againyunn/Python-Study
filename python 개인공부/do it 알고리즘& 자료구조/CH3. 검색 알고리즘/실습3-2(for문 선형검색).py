from typing import Sequence, Any

def Sequence_search(a : Sequence, key: Any):
    for i in range(len(a)):
        if a[i]==key:
            return i
    else:
        return -1


if __name__=='__main__' :

    print('실수를 검색합니다.')
    print('주의: "End"를 입력하면 종료합니다.')

    number = 0
    x = []

    while True:
        s = input(f'x[{number}] = ') #string의 데이터 형으로 list s 를 입력받기
        if s =='End':
            break
        x.append(float(s)) #입력받은 list s의 데이터 형을 float으로 변경하여 list x에 저장
        number+=1

    key= float(input('\n검색할 값을 입력하세요. : '))

    idx= Sequence_search(x, key)
    if idx == -1:
        print('검색 값을 가진 원소가 없습니다.')
    else:
        print(f'검색값은 x[{idx}]에 있습니다.')






        