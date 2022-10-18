import heapq, random

def solve(A, k): # return k-th smallest key, 1 <= k <= n
    num = len(A) // 2
    if num >= k:
        for a in range(k):
            answer = heapq.heappop(A)
        return answer
    else:
        tmp = [-x for x in A]
        heap_max = heapq.heapify(tmp)
        for b in range(num - k):
            answer = heapq.heappop(heap_max)
        answer *= -1
        return answer

k = int(input())
A = [int(x) for x in input().split()]
heapq.heapify(A) # A is now a min-heap
print(solve(A, k))



''' 힙이 최대힙/최소힙 두가지 경우로 구현될 수 있음을 활용하여 최악의 경우(최소힙일 때 가장 큰 값을 호출할 경우) 수행시간을 단축한 알고리즘

	case1
	k가 리스트A의 원소수//2 와 같거나 작은 경우:
	T(N)=1/2NlogN+3
	O(N)=NlogN

	case2
	k가 리스트A의 원소수//2보다 큰 경우:
	T(N)=1/2NlogN+2N+4
	O(N)=NlogN

	즉 최악의 경우인 len(A)//2+1=k 를 인자로 받아, 리스트A에서 k번째로 작은 수를 호출하는 경우에도
	T(N)=1/2NlogN+2N+4의 연산으로 답을 구할 수 있다.

	처음 heapq모듈을 사용하여 구현한 단순 알고리즘은
	def solve(A, k):
		for a in range(k):
			answer=heapq.heappop(A)
		return answer
	의 코드였으나, 처음 알고리즘은 T(N)=NlogN의 수행시간이 필요했다. 
	그렇기에 k=n의 경우 for반복문을 통해 모든 원소를 heappop하는 연산이 필요해, k의 수가 커질수록 알고리즘의 수행시간이 증가했다.
	이와 달리 현알고리즘(case1, case2로 구분)은 k=n인 경우에 단 한번의 heappop연산으로 답을 구할 수 있게 개선되었다.
	------------------------------------------------------------------

	(* 직접 구현한 알고리즘을 현알고리즘이라고 표현하였습니다)
	또한 Algorithm_SORT는 O(NlogN)으로 k의 크기에 비례하는 수행시간을 보이며 처음 알고리즘(단순 힙 사용)과 동일한 수행시간과 한계점을 갖는다.

	Algorithm_QUICK보다는 현 알고리즘이 평균적인 경우에 조금 더 느리지만, 두 알고리즘의 Worst Case를 비교하면 현 알고리즘이 더 효율적이다.
	마지막으로, Algorithm_MOM보다 전체적인 속도가 느리지만, 코드 구현 측면에서 현 알고리즘이 쉽고 간편하며, 숨겨진 상수시간의 연산이 적다는 특징이 있다.
'''

#     for a in range(k):
#         answer=heapq.heappop(A)
#     return answer
#
#
#
# k = int(input())
# A = [int(x) for x in input().split()]
# heapq.heapify(A)  # A is now a min-heap
# print(solve(A, k))

# k=6
# A=[]
# for i in range(40):
#     a=random.randint(1,100)
#     A.append(a)
#
# print(f'힙정렬 전: {A}')
# heapq.heapify(A)
# print(f'힙정렬 후: {A}')
#
# for i in range(k-1):
#     heapq.heappop(A)
# print(heapq.heappop(A))

