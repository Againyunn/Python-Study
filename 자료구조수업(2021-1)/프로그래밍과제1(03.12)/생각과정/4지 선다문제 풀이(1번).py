def solution():
    asw=input('문제별 정답을 입력하시오: ').split() #정답 입력
    score=input('문제별 배점을 입력하시오: ').split() #배점 입력
    submit=input('학생의 답을 입력하시오: ').split() #제출한 답안지 입력

    num=len(asw) #문제의 문항수
    result=[] #맞춘 문제의 수 기록
    for i in range(num):
        if asw[i]==submit[i]: #정답이 맞은 문제 문항을 기록
            result.append(i+1)
    answer=print(f'정답을 맞춘 문제: {result}번 입니다.')
    return answer

if __name__=="__main__":
    sol=solution()
    print(sol)


    