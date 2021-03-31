def solution(info, query):
    #사전 작업 : info의 " "로 묶인 원소를 data의 원소로 / query의 " "로 묶인 원소를 inquire의 원소로
    data=[] #info의 데이터를 나누어 담을 빈 리스트 (짝수의 원소 개수만큼만 data 리스트로 생성)
    num1=len(info)//2
    for i in range((2*num1)): #[와 , 로 인해 split에서 걸러질 때 [ 와 ,를 하나의 원소로 인식 -> 짝수원소만 유의미한 값
        transform11=str(info[i]).strip('[ ,"]')
        if transform11 not in ('['):
            transform13=transform11.split()
            data.append(transform13)

    inquire=[] #query의 요구사항을 나누어 담을 빈 리스트 (짝수의 원소 개수만큼만 inquire 리스트로 생성)
    num2=len(query)//2
    for i in range((2*num2)):
        transform21=str(query[i]).strip('[ ,"]')
        transform23=transform21.replace("and","")
        if transform23 not in ('[') :
            transform24=transform23.split()
            inquire.append(transform24)

    #질문 사항의 개수
    inquireNum=len(inquire)
    dataNum=len(data)

    #조회할 질문의 명단 만들기(언어~점수)
    score=[None] * inquireNum

    #각 쿼리(요구사항)별 체크사항
    check=[0]*inquireNum #각 원소가 각각의 쿼리 별 체크사항

    #inquire리스트의 원소가 지칭하는 바 
    # inquire[a][0: 언어 , 1: 직군, 2: 경력, 3: 소울푸드, 4:점수]
    for a in range(inquireNum):
        #1)프로그래밍 언어 구분:  
        if inquire[a][0] != '-': #미선택이 아닌 경우에만 check +1
            check[a]+=1

        #2)직군 구분:
        if inquire[a][1] != '-':
            check[a]+=1

        #3)경력 구분:
        if inquire[a][2] != '-':
            check[a]+=1

        #4)소울푸드 구분:
        if inquire[a][3] != '-':
            check[a]+=1

        #5)점수 조회:
        score[a] = inquire[a][4]
        check[a]+=1
    score=list(map(int,score))

    #1중 : 각 원소 = data의 지원자 개체 , 2중 : 각 원소 = inquire의 질문 개체마다의 점수
    #퀴리별 체크사항에 부합하는 info 판별하여 count에 기록
    count=[0]*dataNum #경우에 따른 명 수를 체크하기 위한 빈 리스트(각 info의 원소가 쿼리별로 얼마나 충족하는 지 판별)
    answer = [0]*inquireNum #질문 개수대로 0 생성(각 index가 질문을 의미)

    count=[0]*dataNum #경우에 따른 명 수를 체크하기 위한 빈 리스트(각 info의 원소가 쿼리별로 얼마나 충족하는 지 판별)
    for i in range(dataNum):
        countMini=[0]*inquireNum
        for j in range(inquireNum): #각 지원자별 체크사항과 부합하는 지 여부 확인
            if inquire[j][0]!='-' and inquire[j][0]==data[i][0]:
                    countMini[j]+=1
            if inquire[j][1]!='-' and inquire[j][1]==data[i][1]:
                    countMini[j]+=1
            if inquire[j][2]!='-' and inquire[j][2]==data[i][2]:
                    countMini[j]+=1
            if inquire[j][3]!='-' and inquire[j][3]==data[i][3]:
                    countMini[j]+=1
            if score[j]<=int(data[i][4]): #score과 같거나 더 큰 점수를 가진 경우
                countMini[j]+=1
            count[i]=countMini
    
    #각 쿼리별 체크사항을 취합한 count와 check(쿼리 요구사항)이 일치하는 지 판별
    answer = [0]*inquireNum #질문 개수대로 0 생성(각 index가 질문을 의미)
    for i in range(inquireNum): 
        for j in range(dataNum): 
            if count[j][i]==check[i]:
                answer[i]+=1
    return answer


info=input("info : ").split('"')
query=input("query : ").split('"')
sol=solution(info,query)
print(sol)