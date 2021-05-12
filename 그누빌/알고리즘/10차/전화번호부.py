

def solution(phone_book):
    answer = True
    length=len(phone_book)
    for i in range(length):
        for j in range(i+1,length):
            if phone_book[j].startswith(phone_book[i]):
                answer=False
                return answer
    
    return answer
#for문에서 중복되는 검색 값 제거(i와 j의 값 설정을 통해)
#각 문장별 O(n)수행시간 측정 후 최소화


def solution2(phone_book): #정답
    answer = True
    dic = {}
    
    #phone_book에 있는 번호를 dic key에 넣기
    for i in phone_book:
        dic[i] = 0
        
    #각 번호를 검사
    for i in phone_book:
        temp = ''
        #해당 번호를 한글자씩 쪼개서 포함여부를 확인
        for j in i:
            temp += j
            #쪼개진 숫자가 dic에 있고 자신의 원래 번호가 아닐 경우
            if temp in dic and temp != i:
                answer = False
    return answer

a=input().split()
print(solution(a))