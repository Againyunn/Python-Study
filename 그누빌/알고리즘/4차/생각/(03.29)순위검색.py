# info 가 조건
# query 가 요구사항
# - 는 미선택을 의미한다.

#################################################
# (아래의 과정을 문제 5개의 질문 변수로 미리 만들기)
# 데이터를 각 리스트에 옮겨 담기
# 각 데이터별 조회할 데이터를 변수에 담기
# 조회할 변수의 질문을 변수로 만들기

# 질문을 if로 묶어서 실행
# 만약 질문이 없어서 - 값인 경우 해당 질문을 건너뛰도록 알고리즘 구현


def solution(info, query):
    #사전 작업 : info의 " "로 묶인 원소를 data의 원소로 / query의 " "로 묶인 원소를 inquire의 원소로
    data=[] #info의 데이터를 나누어 담을 빈 리스트 (짝수의 원소 개수만큼만 data 리스트로 생성)
    num1=len(info)//2
    for i in range((2*num1)): #[와 , 로 인해 split에서 걸러질 때 [ 와 ,를 하나의 원소로 인식 -> 짝수원소만 유의미한 값
        transform11=str(info[i])
        transform12=transform11.strip('[ ,"]')
        if transform12 not in ('['):
            transform13=transform12.split() #str(info[i])
            data.append(transform13)

    inquire=[] #query의 요구사항을 나누어 담을 빈 리스트 (짝수의 원소 개수만큼만 inquire 리스트로 생성)
    num2=len(query)//2
    for i in range((2*num2)):
        transform21=str(query[i])
        transform22=transform21.strip('[ ,"]')
        if transform22 not in ('[') :
            transform23=transform22.split()
            inquire.append(transform23)

    for i in range(len(inquire)): #inquire 리스트 내의 'and'제거 구문
        num3=len(inquire[i])
        for j in range(num3):
            try:
                if inquire[i][j]=='and':
                    inquire[i].pop(j)
            except IndexError:
                    break             
    

    #조회할 질문의 명단 만들기(언어~점수)
    language=[None] * len(inquire)
    position=[None] * len(inquire)
    career=[None] * len(inquire)
    food=[None] * len(inquire)
    score=[None] * len(inquire)

    #입력 가능한 옵션모음(언어~음식)
    allLanguage=['cpp','java','python','-']
    allPosition=['backend','frontend','-']  
    allCareer=['junior','senior','-']
    allFood=['chicken','pizza','-']

    #각 쿼리(요구사항)별 체크사항
    check=[0]*len(inquire) #각 원소가 각각의 쿼리 별 체크사항

    for a in range(len(inquire)):
        #1)프로그래밍 언어 구분: 
        languageAsked=allLanguage.index(inquire[a][0]) #질문에서 묻는 언어를 langauge에 저장
        language[a]=allLanguage[languageAsked]
        if language[a] != '-': #미선택이 아닌 경우에만 check +1
            check[a]+=1

        #2)직군 구분:
        positionAsked=allPosition.index(inquire[a][1])
        position[a]=allPosition[positionAsked]
        if position[a] != '-':
            check[a]+=1

        #3)경력 구분:
        careerAsked=allCareer.index(inquire[a][2])
        career[a]=allCareer[careerAsked]
        if career[a] != '-':
            check[a]+=1

        #4)소울푸드 구분:
        foodAsked=allFood.index(inquire[a][3])
        food[a]=allFood[foodAsked]
        if food[a] != '-':
            check[a]+=1

        #5)점수 조회:
        score[a] = inquire[a][4]
        check[a]+=1

    ##이쪽 설계를 바꿀 필요가 있음  -> 각 문제(원소)별 체크사항을 지원자의 정보와 1대1 대응하는 형태로 재설계필요
    #어떻게든 결국 2중 리스트 사용해야 한다. 
    #1중 : 각 원소 = data의 지원자 개체 , 2중 : 각 원소 = inquire의 질문 개체마다의 점수
    #퀴리별 체크사항에 부합하는 info 판별하여 count에 기록
    count=[0]*len(data) #경우에 따른 명 수를 체크하기 위한 빈 리스트(각 info의 원소가 쿼리별로 얼마나 충족하는 지 판별)
    for i in range(len(data)):
        countMini=[0]*len(inquire)
        for j in range(len(inquire)): #각 지원자별 체크사항과 부합하는 지 여부 확인
            if language[j]!='-': 
                if language[j]==data[i][0]:
                    countMini[j]+=1
            if position[j]!='-': 
                if position[j]==data[i][1]:
                    countMini[j]+=1
            if career[j]!='-':
                if career[j]==data[i][2]:
                    countMini[j]+=1
            if food[j]!='-':
                if food[j]==data[i][3]:
                    countMini[j]+=1
            scoreTransform=list(map(int,score))
            dataTransform=int(data[i][4])
            if scoreTransform[j]<=dataTransform: #score과 같거나 더 큰 점수를 가진 경우
                countMini[j]+=1
            count[i]=countMini
    
    #각 쿼리별 체크사항을 취합한 count와 check(쿼리 요구사항)이 일치하는 지 판별
    answer = [0]*len(inquire) #질문 개수대로 0 생성(각 index가 질문을 의미)
    for i in range(len(check)): 
        for j in range(len(count)): 
            if count[j][i]==check[i]:
                answer[i]+=1

    return answer


info=input("info : ").split('"')
query=input("query : ").split('"')
sol=solution(info,query)
print(sol)