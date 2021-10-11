def heapify_down(A, k, n):
    while 2*k + 1 < n:  #자식노드가 있는 지 확인
        L = 2 * k + 1 #왼쪽 자식노드
        R = 2 * k +2 #오른쪽 자식노드

        if L < n and A[L] > A[k]: #왼쪽 자식노드 체크
            m = L
        else:
            m = k

        if R < n and A[R] > A[m]: #오른쪽 자식노드 체크
            m = R

        # m = A[k], A[L], A[R] 중 최대 값의 인덱스
        if m != k: # 큰 값을 가지는 인덱스로 변경
            A[k], A[m] = A[m], A[k]
            k = m
        else: #현 가장 앞의 index가 최대이면 반복 정지
            break

def make_heap(A):
    n = len(A)
    for k in range(n-1, -1, -1):
        heapify_down(A,k,n)

def heap_sort(A):
    n = len(A)
    for k in range(len(A)-1, -1, -1):
        A[0], A[k] = A[k], A[0]
        n = n-1
        heapify_down(A,0,n)


# def delete_max(self):
#     if len(self.A) == 0:
#         return None
#     key = self.A[0]
#     self.A[0] , self.A[len(self.A)-1] = self.A[len(self.A)-1], self.A[0]
#     self.A.pop()
#     heapify_down(0, len(self.A))
#     return key


A = [-10, 30, 20, -20, 50]
make_heap(A)
print(A)
heap_sort(A)
print(A)