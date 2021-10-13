def merge(A, i, j, k, l): #j+1 = k여야 한다.
    B=[]
    while i<=j and k<=l:
        if A[i] <= A[j]:
            B.append(A[i])
            i+=1
        else:
            B.append(A[j])
            j+=1

    for a in range(i, j+1):
        B.append(A[a])
    for b in range(k,l+1):
        B.append(A[b])
    for c in range(i, l+1):
        A[c]=B[c-i]

# i <= j and j < k <= l
# 정렬된 두 부분 A[i..j]와 A[k..l]을 merge하는 함수

# def m_sort(A, first, last):
# 3-way merge sort - merge 함수를 이용해 적절히 합병한다








def check(A):
    for i in range(1, len(A)):
        if A[i - 1] > A[i]:
            return False
    return A[0] + A[(len(A) // 2)] + A[-1]


A = [int(x) for x in input().split()]
m_sort(A, 0, len(A) - 1)
print(check(A))