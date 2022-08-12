def selection_sort(self, A):
    n = len(A)

    for i in range(n-1):
        least = i
        for j in range(i+1, n):
            if(A[j] < A[least]):
                least = j
            
        A[i], A[least] = A[least], A[i]
        
