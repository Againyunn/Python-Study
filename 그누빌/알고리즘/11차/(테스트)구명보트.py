def solution(people, limit):
    start=0
    last=len(people)-1 #while문 내의 index 연산 목적
    people.sort()
    people.reverse() #내림차순 정렬: start(앞) index 부터 1개씩 증가하며 비교 목적
    Check=0
    
    while start<last:
        Sum=people[start]+people[last]
        if Sum>limit: #조건 부합x (start index 원소만 탑승)
            start+=1
            
        else: # start, last index 원소 모두 탑승
            start+=1
            last-=1
        Check+=1 #보트 이동 횟수
        
    if start==last: #while문 비교 연산 후 남은 원소가 있는 경우 처리용
        Check+=1

    return Check

people=input().split()
limit=input()
sol=solution(people, limit)
print(sol)