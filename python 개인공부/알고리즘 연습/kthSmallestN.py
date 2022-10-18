# import heapq


# def findKth(A):
#     result = []
#     S = []  # max_heap
#     L = []  # min_heap
#     result.append(A[0])
#     for i in range(1,len(A)):
#         if i!=0 and i%3==0:
#             k=i
#             if not S or -S[0] >= i:
#                 heapq.heappush(S, -i)

#             else:
#                 heapq.heappush(L, i)

#             if len(S) > k:
#                 heapq.heappush(L, -heapq.heappop(S))
#             elif len(S) < k and L:
#                 heapq.heappush(S, -heapq.heappop(L))

#             result.append(-S[0] if len(S) >= k else -1)

#     return result

# A=list(map(int,input().split()))
# print(findKth(A))

import heapq
from sys import stdin

ans = 0
A = list(map(int, stdin.readline().split()))
 
B = []
for i in range(len(A)):
   B.append(A[i])
   C = B[:]
   heapq.heapify(C)
   for j in range(i//3):
      heapq.heappop(C)
   ans += C[0]
print(ans)