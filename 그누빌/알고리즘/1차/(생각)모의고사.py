from typing import Sequence

def solution(q, num1, num2, num3 : Sequence):
    
    #q=list(map(int,q))
    num1 = list(map(int,num1)) #1번 수포자의 정답 문제
    num2 = list(map(int,num2)) #2번 수포자의 정답 문제
    num3 = list(map(int,num3)) #3번 수포자의 정답 문제

    r1=0 #1번 수포자의 정답 횟수 기록
    r2=0 #2번 수포자의 정답 횟수 기록
    r3=0 #3번 수포자의 정답 횟수 기록
    for i in range(len(q)):
        if q[i] == num1[i]:
            r1+=1
        if q[i] == num2[i]:
            r2+=1
        if q[i] == num3[i]:
            r3+=1

    winner = []
    if r1> r2:
        if r1>r3:
            winner.append(1)
        elif r1<r3:
            winner.append(3)
        else: #r1==r3
            winner.append(1)
            winner.append(3)
    elif r2> r1:
        if r2>r3:
            winner.append(2)
        elif r2<r3:
            winner.append(3)
        else:
            winner.append(2)
            winner.append(3)
    else:#r1=r2인 경우
        if r1==r3:
            winner.append(1)
            winner.append(2)
            winner.append(3)
        else:
            winner.append(1)
            winner.append(2)
    print(winner)

if __name__=='__main__':
    while True:
        q = list(input('시험의 답을 입력하시오. : '))
        q=list(map(int,q))
        for i in range(len(q)):
            if 1<=q[i]<=5:
                break
        break

    num1 = list(input('1번 수포자의 답을 입력하시오. : '))    
    num2 = list(input('2번 수포자의 답을 입력하시오. : '))  
    num3 = list(input('3번 수포자의 답을 입력하시오. : ')) 
    
    solution(q, num1, num2, num3)

