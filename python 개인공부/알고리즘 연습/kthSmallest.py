import heapq
from sys import stdin
import time # time 라이브러리 import

# A=list(map(int, stdin.readline().split()))
A =[]
for i in range(10000):
    A.append(i)

start = time.time() # 시작

result = A[0]
S = []
A_len = len(A)

for i in range(A_len):
    S.append(A[i])
    L = S[:]
    heapq.heapify(L) 

    # heap 연산
    k = i//3 + 1
    num = len(L) // 2 
    this_kth = 0
    # 최소 heap
    if num >= k: 
        for _ in range(k):
            this_kth = heapq.heappop(L)
        result += this_kth
    # 최대 heap
    else:
        tmp = [-x for x in L]
        heap_max = heapq.heapify(tmp)
        for _ in range(num - k):
            this_kth = heapq.heappop(heap_max)
        this_kth *= -1
        result += this_kth
    
print(result)
print(f"{time.time()-start:.4f} sec") # 종료와 함께 수행시간 출력
