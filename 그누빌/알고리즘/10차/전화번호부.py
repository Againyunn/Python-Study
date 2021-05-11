

def solution(phone_book):
    answer = True
    length=len(phone_book)
    for i in range(length):
        for j in range(i+1,length):
            if phone_book[j].startswith(phone_book[i]):
                answer=False
                break
    
    return answer
#for문에서 중복되는 검색 값 제거(i와 j의 값 설정을 통해)
#각 문장별 O(n)수행시간 측정 후 최소화

a=input().split()
print(solution(a))