def pin_num(stick, n):
    stick.sort(key = lambda time : time[1] ) # 길이가 짧은 막대의 순서대로 오름차순 배열 O(n log n)

    pin = 0 # 사용한 핀의 개수
    last_finish = 0 # 방금 꽂은 막대의 부분(= 꽂힌 막대를 제외한 남은 막대들 중 가장 끝 부분이 짧은 막대의 끝 부분)
    for i in range(n): # O(n)
        if last_finish < stick[i][0]: # 최근 끝 부분 < 시작 부분 : 같은 막대에 중복으로 꽂는 것 방지
            last_finish = stick[i][1] # 꽂아야 할 막대의 끝 부분
            pin += 1
    return pin

n = int(input())
stick = []
for i in range(n):
    stick.append(list(map(int, input().split())))
print(pin_num(stick, n))
