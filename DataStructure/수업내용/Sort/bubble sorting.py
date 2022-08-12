def bubble_sort(self, A): #파이썬 식 코딩
    n = len(A)

    for i in range(n-1, 0, -1):
        bChanged = False
        for j in range(i):
            if(A[j] > A[j+1]):
                A[j], A[j+1] = A[j+1], A[j]
                bChanged = True
        if not bChanged:
            break

def bubble_sort2(self, A): #자바 식 코딩
    n = len(A)
    for i in range(n):
        for j in range(n-1):
            if A[j]> A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                