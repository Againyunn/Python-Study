def count1(L,x):
    cnt=0
    for item in L:
        if item == x:
            cnt +=1
    return cnt

#list method count
def count2(L, x):
    return L.count(x) #x가 나타난 횟수를 계산해주는 list패키지의 메소드 - 파이썬의 라이브러리

#recursion
#리스트 L[0]부터 L[n-1]까지 원소 중 x와 같은 원소를 구하는 재귀함수 코드
def count3(L, x, n):
    if n ==0:
        return 0
    elif L[n-1] == x:
        return count3(L, x, n-1)+1
    else:
        return count3(L, x, n-1)
#함수 테스트용 코드:
L=[20, 30, 15, 5, 15, 15, 50, 20, 30, 15]
x=15

print(f'count1의 경우 : {count1(L,x)}')

print(f'count2의 경우 : {count2(L,x)}')

print(f'count3의 경우 : {count3(L,x,len(L))}')