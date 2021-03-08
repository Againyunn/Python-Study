def solution(answers):
    q=answers
    num1 = [1,2,3,4,5] #1번 수포자의 정답 문제
    num2 = [2,1,2,3,2,4,2,5] #2번 수포자의 정답 문제
    num3 = [3,3,1,1,2,2,4,4,5,5] #3번 수포자의 정답 문제
    r1=0 #1번 수포자의 정답 횟수 기록
    r2=0 #2번 수포자의 정답 횟수 기록
    r3=0 #3번 수포자의 정답 횟수 기록
    for i in range(len(q)):
        if q[i] == num1[i%5]:
            r1+=1
        if q[i] == num2[i%8]:
            r2+=1
        if q[i] == num3[i%10]:
            r3+=1
    winner = []
    if r1> r2:
        if r1>r3:
            winner=[1]
        elif r1<r3:
            winner=[3]
        else: #r1==r3
            winner=[1,3]
    elif r2> r1:
        if r2>r3:
            winner=[2]
        elif r2<r3:
            winner=[3]
        else:
            winner=[2,3]
    else:#r1=r2인 경우
        if r1==r3:
            winner=[1,2,3]
        else:
            winner=[1,2]
    return winner