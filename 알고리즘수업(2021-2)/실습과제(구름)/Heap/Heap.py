class Heap:
    def __init__(self, L=[]):
        self.A = L
        self.make_heap(self.A)

    def __str__(self):
        return str(self.A)

    def __len__(self):
        return len(self.A)

    def heapify_down(self, k, n):
        while 2 * k + 1 < n:
            L, R = 2 * k + 1, 2 * k + 2
            if L < n and self.A[L] > self.A[k]:
                m = L
            else:
                m = k
            if R < n and self.A[R] > self.A[m]:
                m = R  # m = A[k], A[L], A[R] 중 최대값의 인덱스
            if m != k:
                self.A[k], self.A[m] = self.A[m], self.A[k]
                k = m
            else:
                break  #

    def make_heap(self):
        n = len(self.A)
        for k in range(n - 1, -1, -1):
            self.heapify_down(k, n)

    def heap_sort(self):
        n = len(self.A)
        for k in range(len(self.A) - 1, -1, -1):
            self.A[0], self.A[k] = self.A[k], self.A[0]
            n = n - 1
            self.heapify_down(0, n)


L = [int(x) for x in input().split()]
H = Heap(L)
H.heap_sort()
print(H)