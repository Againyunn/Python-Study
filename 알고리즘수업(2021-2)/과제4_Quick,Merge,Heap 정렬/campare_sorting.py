import random, timeit

###세가지 정렬함수를 위한 코드 작성
def quick_sort(A, first, last):
    global Qc
    global Qs

    if first >= last:
        Qc += 1  # 비교
        return
    left = first +1
    right = last
    pivot = A[first]


    while left <= right:
        while left <= last and A[left] < pivot: #유효한 경우(pivot 옆의 왼쪽 인덱스 번호가 마지막 인덱스 번호와 같거나 작은 경우) +
            left+=1
            Qc += 1  # 비교
        while right > first and A[right] > pivot:
            right-=1
            Qc += 1  # 비교
        if left <= right:
            Qc += 1  # 비교
            A[left], A[right] = A[right], A[left]
            Qs += 1  # 교환
            left+=1
            right-=1

    A[first], A[right] = A[right], A[first]
    Qs += 1  # 교환
    quick_sort(A, first, right-1)
    quick_sort(A, right+1, last)


def merge_sort(B, first, last):
    global Mc
    global Ms
    if first >= last:
        Mc += 1  # 비교
        return
    merge_sort(B, first, (first+last)//2)
    merge_sort(B, (first+last)//2+1, last)

    mid = (first + last) // 2
    i, j = first, mid + 1
    tmp = []
    while i <= mid and j <= last:
        if B[i] <= B[j]:
            Mc += 1  # 비교
            tmp.append(B[i])
            i += 1
        else:
            Mc += 1  # 비교
            tmp.append(B[j])
            j += 1

    for a in range(i, mid + 1):
        Ms += 1  # 교환
        tmp.append(B[a])
    for b in range(j, last + 1):
        Ms += 1  # 교환
        tmp.append(B[b])
    for c in range(first, last + 1):
        Ms += 1  # 교환
        B[c] = tmp[c - first]


def heap_sort(C):
    global Hc
    global Hs

    n = len(C)
    for k in range(n - 1, -1, -1):
        while 2 * k + 1 < n:  # 자식노드가 있는 지 확인
            Hc += 1 #비교
            L = 2 * k + 1  # 왼쪽 자식노드
            R = 2 * k + 2  # 오른쪽 자식노드

            if L < n and C[L] > C[k]:  # 왼쪽 자식노드 체크
                Hc += 1  # 비교
                m = L
            else:
                Hc += 1  # 비교
                m = k

            if R < n and C[R] > C[m]:  # 오른쪽 자식노드 체크
                Hc += 1  # 비교
                m = R

            # m = A[k], A[L], A[R] 중 최대 값의 인덱스
            if m != k:  # 큰 값을 가지는 인덱스로 변경
                Hs += 1  # 교환
                C[k], C[m] = C[m], C[k]
                k = m
            else:  # 현 가장 앞의 index가 최대이면 반복 정지
                break

    for k in range(len(C)-1, -1, -1):
        Hs += 1  # 교환
        C[0], C[k] = C[k], C[0]
        n = n-1
        k = 0
        while 2 * k + 1 < n:  # 자식노드가 있는 지 확인
            Hc += 1  # 비교
            L = 2 * k + 1  # 왼쪽 자식노드
            R = 2 * k + 2  # 오른쪽 자식노드

            if L < n and C[L] > C[k]:  # 왼쪽 자식노드 체크
                Hc += 1  # 비교
                m = L
            else:
                Hc += 1  # 비교
                m = k

            if R < n and C[R] > C[m]:  # 오른쪽 자식노드 체크
                Hc += 1  # 비교
                m = R

            # m = A[k], A[L], A[R] 중 최대 값의 인덱스
            if m != k:  # 큰 값을 가지는 인덱스로 변경
                Hs += 1  # 교환
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
print("Merge sort:")
print("time =", timeit.timeit("merge_sort(B, 0, n-1)", globals=globals(), number=1))
print(" comparisons = {:10d}, swaps = {:10d}\n".format(Mc, Ms))

print("Heap sort:")
print("time =", timeit.timeit("heap_sort(C)", globals=globals(), number=1))
print(" comparisons = {:10d}, swaps = {:10d}\n".format(Hc, Hs))

# 진짜 정렬되었는 지 check한다. 정렬되지 않았다면,assert 함수 fail됌
assert(check_sorted(A))
assert(check_sorted(B))
assert(check_sorted(C))
