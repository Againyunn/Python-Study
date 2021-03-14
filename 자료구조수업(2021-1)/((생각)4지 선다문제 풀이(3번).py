def solution():
    asw=input('문제별 정답을 입력하시오: ').split() #정답 입력
    score=input('문제별 배점을 입력하시오: ').split() #배점 입력
    num_Paper=int(input("제출한 답안지의 갯수를 입력하시오: ")) #제출한 답안지 수 
    submit=[None]*num_Paper#제출한 답안지의 빈 2차 배열 list x 문제지 갯수

    for i in range(num_Paper):
        submit[i]=input('문제지 별 입력한 답을 기입하시오: ').split() #변수i로 답안을 입력받아 제출한 답안지 submit[]에 저장
        submit[i]=list(map(int,submit[i]))
    #list들의 데이터 형태를 integer로 변경
    asw=list(map(int,asw))
    score=list(map(int,score))
    
    num_Test=len(asw) #문제의 문항수
    error=[0]*num_Test #문항 수 만큼 원소 생성
    for i in range(num_Test):
        for k in range(num_Paper): #문제지 번호 측정용
            if submit[k][i] != asw[i]: #각 문제지 별로 틀린 문항 확인
                error[i]+=1  #문항별(index) 틀린 문제 기록
    print(error)

    for i in range(num_Test):
        e=error[i]
        error[i]=[i+1,e]#각 원소 i 별 [문항번호, 틀린 횟수]

    for i in range(num_Test):
        if       
    #error=list(map(int,error))
    
    error_Score=max(error)
    error_Num=error.index(error_Score)+1 #index는 기본적으로 0부터 n-1까지 이므로 제출한 시험지의 순서를 1~n이라고 보았을 때, +1 처리

    return error_Num , error_Score 

if __name__=="__main__":
    sol=solution()
    print(sol)


    
    