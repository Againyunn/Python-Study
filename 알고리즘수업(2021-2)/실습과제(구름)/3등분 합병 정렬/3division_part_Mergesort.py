

def m_sort(A, first, last):
    # 3-way merge sort - merge 함수를 이용해 적절히 합병한다
    if first>= last:
        return

    oneThird=(first+last)//3
    twoThird=(first+last)//3*2

    m_sort(A, first, oneThird) #3등분의 첫번째
    m_sort(A, oneThird+1, twoThird) #3등분의 두번쨰
    m_sort(A, twoThird+1, last) #3등분의 세번째
    print(A)

    i=first
    j=oneThird
    k=oneThird+1
    l=twoThird
    merge(A, i, j, k, l)

    i = first
    j = twoThird
    k = twoThird+1
    l = last
    merge(A, i, j, k, l)

def merge(A, i, j, k, l): #j+1 = k여야 한다.
    B=[]
    while i<=j and k<=l:
        if A[i] <= A[k]:
            B.append(A[i])
            i+=1
        else:
            B.append(A[j])
            j+=1

    for a in range(i, j+1):
        B.append(B[a])
    for b in range(k,l+1):
        B.append(B[b])
    for c in range(i, l+1):
        A[c]=B[c-i]

# i <= j and j < k <= l
# 정렬된 두 부분 A[i..j]와 A[k..l]을 merge하는 함수


def check(A):
    for i in range(1, len(A)):
        if A[i - 1] > A[i]:
            return False
    return A[0] + A[(len(A) // 2)] + A[-1]


A = [int(x) for x in input().split()]
m_sort(A, 0, len(A) - 1)
#######
print("실제 값")
print(check(A))
#################
print(A)