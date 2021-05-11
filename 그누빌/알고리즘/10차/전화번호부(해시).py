hash_table = list([i for i in range(10)])
hash_table

def hash_func(key):
    return key % 5

def get_data(data):
    key = ord(data[0])
    hash_address = hash_func(key)
    return hash_table[hash_address]



def solution(phone_book):
    HashBook = list([i for i in range(len(phone_book))])
    answer = True
    for i in phone_book:
        for j in phone_book:
            if j.find(i) ==0:
                answer=False
    
    return answer
#for문에서 중복되는 검색 값 제거(i와 j의 값 설정을 통해)
#각 문장별 O(n)수행시간 측정 후 최소화

a=input().split()
print(solution(a))