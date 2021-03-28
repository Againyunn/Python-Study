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
    #사전 작업 : info의 " "로 묶인 원소를 data의 원소로 담기 
    data=[] #info의 데이터를 나누어 담을 빈 리스트 (짝수의 원소 개수만큼만 data 리스트로 생성)
    num1=len(info)//2
    for i in range((2*num1)-1): #[와 , 로 인해 split에서 걸러질 때 [ 와 ,를 하나의 원소로 인식 -> 짝수원소만 유의미한 값
        transform1=str(info[i])
        transform2=transform1.strip('[ ,"]')
        if transform2 not in ('[' and 'None'):
            transform3=transform2.split() #str(info[i])
            data.append(transform3)
    print(data)
    #####완성#####
    inquire=[None]*len(query) #query의 요구사항을 나누어 담을 빈 리스트
    for i in range(len(query)):
        word=str(query[i]).split()
        print(word)
        word.remove("and") #inquire에서 "and" 원소를 모두 제거
        inquire[i]=word

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
        language=allLanguage.index(inquire[a]) #질문에서 묻는 언어를 langauge에 저장
        language[a]=allLanguage[language]
        if language[a] != '-': #미선택이 아닌 경우에만 check +1
            check[a]+=1

        #2)직군 구분:
        position=allPosition.index(inquire[a])
        position[a]=allPosition[position]
        if position[a] != '-':
            check[a]+=1

        #3)경력 구분:
        career=allCareer.index(inquire[a])
        career[a]=allCareer[career]
        if career[a] != '-':
            check[a]+=1

        #4)소울푸드 구분:
        food=allFood.index(inquire[a])
        food[a]=allFood[food]
        if food[a] != '-':
            check[a]+=1

        #5)점수 조회:
        score[a] = data[a][4]
        check[a]+=1

    #퀴리별 체크사항에 부합하는 info 판별하여 count에 기록
    count=[0]*len(info) #경우에 따른 명 수를 체크하기 위한 빈 리스트(각 info의 원소가 쿼리별로 얼마나 충족하는 지 판별)
    for i in range(len(info)): #각 지원자별 체크사항과 부합하는 지 여부 확인
        #for j in range(len(inquire)):
        if language[i]!='-': 
            if language[i]==data[i][0]:
                count[i][0]=1
            else:
                count[i][0]=0
        if position[i]!='-': 
            if position[i]==data[i][1]:
                count[i][1]=1
            else:
                count[i][0]=0
        if career[i]!='-':
            if career[i]==data[i][2]:
                count[i][2]=1
            else:
                count[i][2]=0
        if food[i]!='-':
            if food[i]==data[i][3]:
                count[i][3]=1
            else:
                count[i][3]=0
        if score[i]<=data[i][4]: #score과 같거나 더 큰 점수를 가진 경우
            count[i][4]=1
        if score[i]>data[i][4]:
            count[i][4]=0 
    
    #각 쿼리별 체크사항을 취합한 count와 check(쿼리 요구사항)이 일치하는 지 판별
    answer = [0]*len(query) #쿼리 개수대로 0 생성
    for r in range(len(query)):
        for s in range(len(info)):
            if check[r]==len(count[s]): #각 쿼리별 check와 지워자별 count가 일치하는 지 확인
                answer[r]+=1
    
        


    #for 구문으로 반복하기 (로직 완성 후 변환하기)
    #우선은 첫문제의 로직을 세우기 위해 [0]의 경우에 데이터 변환부터 처리

    #질문1의 유형 정리
    #question1 = language in data[a][0] #a번째 질문의 언어가 languge와 맞는 지 확인

    #질문2의 유형 정리
    #question2 = position in data[a][1] #a번째 질문의 직군이 position과 맞는 지 확인

    #질문3의 유형 정리
    #question3 = career in data[a][2]

    #질문4의 유형 정리
    #question4 = food in data[a][3]
    return answer


info=input("info : ").split('"')
query=input("query : ").split('"')
sol=solution(info,query)
print(sol)