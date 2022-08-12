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

    for i in range(num_Test):
        e=error[i]
        error[i]=[i+1,e]#각 원소 i 별 [문항번호, 틀린 횟수]

    rank=sorted(error, key = lambda x :x[1], reverse = True)
    #rank.sort(reverse = True)

    result=[]#결과 값을 담을 list (최고 오답률 문항이 여러개인 경우 )
    max=0 #최대 오답 기록

    for i in range(len(rank)):
        if i==0:
            max=rank[0][1]#오답률 기준 내림차순으로 정렬된 원소의 최고(가장 먼저 값)을 max로 우선 지정
            result.append(rank[0][0]) #첫번째 문항의 번호를 result의 원소로 추가
        if i!=0: #i가 0이 아닌 모든 경우
            if rank[i][1]>=max: #만약 각 원소가 max와 같거나 더 크다면
                result.append(rank[i][0]) #max와 값이 같은 문항을 result의 원소로 추가
            max=max    

    return result

if __name__=="__main__":
    sol=solution()
    print(sol)


    
    