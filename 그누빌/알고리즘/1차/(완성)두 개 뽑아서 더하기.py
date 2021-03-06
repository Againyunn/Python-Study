from typing import Sequence

def solution(n : Sequence):
    n=list(map(int,n))
    r1=[]#r1은 두 원소의 합을 담은 리스트   --> 굳이 none값으로 빈리스트를 경우의 수(조합)만큼 생성하여 차후에 원소에 값을 추가할 필요 없이 바로 빈리스트 생성 후 나중에 append로 추가하는 방법 이용가능
    m=0 #두원소의 합(각각의 값)

    for i in range(len(n)):
        for j in range(len(n)):
            if i!=j:
                m=n[i]+n[j]
                r1.append(m)
    r2=[] #r2는 중복된 값을 제거한 최종 출력 list
    for i in r1:
        if i not in r2:
            r2.append(i)
    r2.sort()
    print(r2)
                
if __name__=='__main__':
    numbers=list(input('배열을 입력하시오.'))
    solution(numbers)