import random

# def heapify_rec(A, n, i):
#     m = i
#     L=2*i+1
#     R=2*i+2
#
#     if L< n and A[i] < A[L]:
#         m = L
#     if R<n and A[m] < A[R]:
#         m = R
#     if m != i:
#         A[i], A[m] = A[m], A[i]
#         heapify(A,n,m)


def heapify_rec(A, n, i):
    while 2*n+1< i:
        m = i
        L=2*i+1
        R=2*i+2

        if L< n and A[i] < A[L]:
            m = L
        if R<n and A[m] < A[R]:
            m = R
        if m != i:
            A[i], A[m] = A[m], A[i]
            n = m



def heapify(A, n, i):
    while 2*n+1 < i:
        L = 2 * i + 1
        R = 2 * i + 2

        if L < n and A[i] < A[L]:
            m = L
        else:
            m = n

        if R < n and A[m] < A[R]:
            m = R

        if m != i:
            A[i], A[m] = A[m], A[i]
            n = m

        else:
            break

def heapSort(A):
    n = len(A)
    for i in range(n//2, -1, -1):
        heapify_rec(A, n, i)

    for i in range(n-1, 0, -1):
        A[i], A[0] = A[0], A[i]
        heapify_rec(A, i, 0)

    for i in range(len(A)):
        print(f'{A[i]} ,')

# def heapSort(A):
#     n = len(A)
#     for i in range(n-1, -1, -1):
#         heapify(A, n, i)
#
#     for i in range(n-1, -1, -1):
#         A[i], A[0] = A[0], A[i]
#         n = n-1
#         heapify(A, i, 0)
#
#     for i in range(len(A)):
#         print(f'{A[i]} ,')


##############################################
def check_sorted(A):
    for i in range(n-1):
        if A[i]>A[i+1]: return False
        return True



####랜덤 입력
n = int(input())
random.seed()
A = []
for i in range(n):
    A.append(random.randint(-1000, 1000))


heapSort(A)
assert(check_sorted(A))
print(A)