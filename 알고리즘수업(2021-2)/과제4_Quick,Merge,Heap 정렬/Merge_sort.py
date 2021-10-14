def merge_sort(A, first, last):
    if first >= last:
        return
    merge_sort(A, first, (first+last)//2)
    merge_sort(A, (first+last)//2+1, last)

    merge_two_sorted(A, first, last)

def merge_two_sorted(A, first, last):
    mid = (first+last)//2
    i, j = first, mid+1

    B=[]
    while i <= mid and j <= last:
        if A[i] <= A[j]:
            B.append(A[i])
            i+=1
        else:
            B.append(A[j])
            j+=1

    for a in range(i, mid+1):
        B.append(A[a])
    for b in range(j, last+1):
        B.append(A[b])
    for c in range(first, last+1):
        A[c] = B[c-first]


def check(A):
    for i in range(1, len(A)):
        if A[i - 1] > A[i]:
            return False
    return A[0] + A[(len(A) // 2)] + A[-1]


A = [int(x) for x in input().split()]
print(f'sort전: {A}')


merge_sort(A, 0, len(A) - 1)
#######

print(check(A))
print(f'sort후: {A}')