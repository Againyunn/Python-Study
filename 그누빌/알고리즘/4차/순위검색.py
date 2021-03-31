def solution(info, query):
    #사전 작업 : info의 " "로 묶인 원소를 data의 원소로 / query의 " "로 묶인 원소를 inquire의 원소로
    data=[] #info의 데이터
    for i in range(len(info)): 
        transform11=str(info[i]).strip('[ ,"]') #info의 각 원소를 str으로 변환 후 불필요한 기호 제거
        if transform11 not in ('['):
            data.append(transform11.split()) #유의미한 값들만 data에 저장
    inquiry=[] #query의 요구사항
    for i in range(len(query)):
        transform21=str(query[i]).strip('[ ,"]')
        transform22=transform21.replace("and","") #query의 각 원소를 str으로 변환 후 불필요한 기호 제거
        if transform22 not in ('[') :
            inquiry.append(transform22.split()) #유의미한 값들만 inquire에 저장

    #개수
    dataNum=len(data) #지원자 수
    inquiryNum=len(inquiry) #요구사항의 수

    #각 쿼리(요구사항)별 체크사항
    check=[0]*inquiryNum #각 원소가 각각의 쿼리 별 체크사항을 의미
    score=[]#점수를 기록용 빈리스트(점수만 integer형이므로 따로 생각)

    #inquire리스트의 원소가 지칭하는 바 
    # inquire 1중 리스트 : 각 원소 = data의 지원자 개체 , 2중 리스트 : 각 원소 = inquire의 요구사항마다의 충족여부
    # inquire[a][0: 언어 , 1: 직군, 2: 경력, 3: 소울푸드, 4:점수]
    # inquire의 요구사항이 '미선택'이 아닌 경우에만 check +1
    for a in range(inquiryNum):
        #1)프로그래밍 언어 구분:  
        if inquiry[a][0] != '-': 
            check[a]+=1
        #2)직군 구분:
        if inquiry[a][1] != '-':
            check[a]+=1
        #3)경력 구분:
        if inquiry[a][2] != '-':
            check[a]+=1
        #4)소울푸드 구분:
        if inquiry[a][3] != '-':
            check[a]+=1
        #5)점수 조회:
        score.append(int(inquiry[a][4])) #inquire은 str타입이므로 int형 변환 후 score저장
        check[a]+=1
    
    # 퀴리별 체크사항에 부합하는 info 판별하여 count에 기록
    count=[0]*dataNum #경우에 따른 명 수를 체크하기 위한 빈 리스트(각 info 원소가 쿼리별로 얼마나 충족하는 지 판별)
    
    for i in range(dataNum):
        countMini=[0]*inquiryNum # 지원자마다 쿼리별 요구사항 충족정도를 기록하기 위한 리스트 
        for j in range(inquiryNum): #각 지원자별 체크사항과 부합하는 지 여부 확인
            if inquiry[j][0]!='-' and inquiry[j][0]==data[i][0]:
                    countMini[j]+=1
            if inquiry[j][1]!='-' and inquiry[j][1]==data[i][1]:
                    countMini[j]+=1
            if inquiry[j][2]!='-' and inquiry[j][2]==data[i][2]:
                    countMini[j]+=1
            if inquiry[j][3]!='-' and inquiry[j][3]==data[i][3]:
                    countMini[j]+=1
            if score[j]<=int(data[i][4]): #score과 같거나 더 큰 점수를 가진 경우
                countMini[j]+=1
            count[i]=countMini
    
    #각 쿼리별 체크사항을 취합한 count와 check(쿼리 요구사항)이 일치하는 지 판별
    answer = [0]*inquiryNum #질문 개수대로 0 생성(각 index가 쿼리의 문항을 의미)
    for i in range(inquiryNum): 
        for j in range(dataNum): 
            if count[j][i]==check[i]:
                answer[i]+=1
    return answer

info=input("info : ").split('"')
query=input("query : ").split('"')
sol=solution(info,query)
print(sol)