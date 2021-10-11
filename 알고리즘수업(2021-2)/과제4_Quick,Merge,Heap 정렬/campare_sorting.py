import random, timeit

###세가지 정렬함수를 위한 코드 작성
def quick_sort(A, first, last):
    if first >= last:
        return
    left = first +1
    right = last
    pivot = A[first]

    while left <= right:
        while left <= last and A[left] < pivot:
            left+=1
        while right > first and A[right] > pivot:
            right-=1
        if left <= right:
            A[left], A[right] = A[right], A[left]
            left+=1
            right-=1

    A[first], A[right] = A[right], A[first]
    quick_sort(A, first, right-1)
    quick_sort(A, right+1, last)


# # def merge_sort(B, first, last):
#
#
#
#

#
def heap_sort(C):
    n = len(C)
    for k in range(n - 1, -1, -1):
        while 2 * k + 1 < n:  # 자식노드가 있는 지 확인
            L = 2 * k + 1  # 왼쪽 자식노드
            R = 2 * k + 2  # 오른쪽 자식노드

            if L < n and C[L] > C[k]:  # 왼쪽 자식노드 체크
                m = L
            else:
                m = k

            if R < n and C[R] > C[m]:  # 오른쪽 자식노드 체크
                m = R

            # m = A[k], A[L], A[R] 중 최대 값의 인덱스
            if m != k:  # 큰 값을 가지는 인덱스로 변경
                C[k], C[m] = C[m], C[k]
                k = m
            else:  # 현 가장 앞의 index가 최대이면 반복 정지
                break

    for k in range(len(C)-1, -1, -1):
        C[0], C[k] = C[k], C[0]
        n = n-1
        k = 0
        while 2 * k + 1 < n:  # 자식노드가 있는 지 확인
            L = 2 * k + 1  # 왼쪽 자식노드
            R = 2 * k + 2  # 오른쪽 자식노드

            if L < n and C[L] > C[k]:  # 왼쪽 자식노드 체크
                m = L
            else:
                m = k

            if R < n and C[R] > C[m]:  # 오른쪽 자식노드 체크
                m = R

            # m = A[k], A[L], A[R] 중 최대 값의 인덱스
            if m != k:  # 큰 값을 가지는 인덱스로 변경
                C[k], C[m] = C[m], C[k]
                k = m
            else:  # 현 가장 앞의 index가 최대이면 반복 정지
                break
    return C



###아래 코드는 고정
def check_sorted(A):
    for i in range(n-1):
        if A[i]>A[i+1]: return False
        return True


Qc, Qs, Mc, Ms, Hc, Hs = 0, 0, 0, 0, 0, 0

n = int(input())
random.seed()
A = []
for i in range(n):
    A.append(random.randint(-1000, 1000))
B = A[:]
C = A[:]

print("")
print("Quick sort:")
print("time =", timeit.timeit("quick_sort(A, 0, n-1)", globals=globals(), number=1))
print(" comparisons = {:10d}, swaps = {:10d}\n".format(Qc, Qs))
#
# print("Merge sort:")
# print("time =", timeit.timeit("merge_sort(B, 0, n-1)", globals=globals(), number=1))
# print(" comparisons = {:10d}, swaps = {:10d}\n".format(Mc, Ms))

print("Heap sort:")
print("time =", timeit.timeit("heap_sort(C)", globals=globals(), number=1))
print(" comparisons = {:10d}, swaps = {:10d}\n".format(Hc, Hs))

# 진짜 정렬되었는 지 check한다. 정렬되지 않았다면,assert 함수 fail됌
assert(check_sorted(A))
# assert(check_sorted(B))
assert(check_sorted(C))
print(A)
print(C)