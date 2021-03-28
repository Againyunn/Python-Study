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
    #사전 작업
    data=[None]*len(info) #info의 데이터를 나누어 담을 빈 리스트
    for i in range(len(info)): #info의 " "로 묶인 원소를 data의 원소로 담기
        data[i]=info[i].split #2중 배열로 저장

    inquire=[None]*len(query) #query의 요구사항을 나누어 담을 빈 리스트
    for i in range(len(query)):
        inquire[i]=query[i].split
        inquire[i].remove('and')

    #조회할 질문의 명단 만들기
    count=[] #경우에 따른 명 수를 체크하기 위한 빈 리스트
    #for 구문으로 반복하기 (로직 완성 후 변환하기)
    for a in range(len(query)):
        #우선은 첫문제의 로직을 세우기 위해 [0]의 경우에 데이터 변환부터 처리
        
        #1)프로그래밍 언어 구분: 
        allLanguage=['cpp','java','python','-'] #전체 프로그래밍 언어
        language=allLanguage.index(inquire[a]) #질문에서 묻는 언어를 langauge에 저장
        #질문1의 유형 정리
        #question1 = language in data[a][0] #a번째 질문의 언어가 languge와 맞는 지 확인

        #2)직군 구분:
        allPosition=['backend','frontend','-']  #전체 직군
        position=allPosition.index(inquire[a])
        #질문2의 유형 정리
        #question2 = position in data[a][1] #a번째 질문의 직군이 position과 맞는 지 확인
        
        #3)경력 구분:
        allCareer=['junior','senior','-']
        career=allCareer.index(inquire[a])
        #질문3의 유형 정리
        #question3 = career in data[a][2]

        #4)소울푸드 구분:
        allFood=['chicken','pizza','-']
        food=allFood.index(inquire[a])
        #질문4의 유형 정리
        #question4 = food in data[a][3]

        #5)점수 조회
        score = data[a][4]













    answer = []
    return answer