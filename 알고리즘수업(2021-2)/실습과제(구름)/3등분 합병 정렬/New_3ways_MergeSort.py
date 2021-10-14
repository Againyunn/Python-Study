def merge(A, i, j, k, l):
    mid=j
    set_i=i
    set_k=k

    tmp=[]
    while set_i <= mid and set_k <= l:
        if A[set_i] <= A[set_k]:
            tmp.append(A[set_i])
            set_i+=1
        else:
            tmp.append(A[set_k])
            set_k+=1

    for a in range(set_i, mid+1):
        tmp.append(A[a])
    for b in range(set_k, l+1):
        tmp.append(A[b])
    for c in range(i, l+1):
        A[c] = tmp[c-i]


def m_sort(A, first, last):
    if last-first <1:
        return


    oneThird=first+(last-first)//3
    twoThird=first+2*((last-first)//3)+1

    m_sort(A, first, oneThird)
    m_sort(A, oneThird+1, twoThird)
    m_sort(A, twoThird+1, last)

    merge(A, first, oneThird, oneThird + 1, twoThird)
    print(f'merge={A}')

    merge(A, first, twoThird, twoThird + 1, last)
    print(f'merge={A}')




def check(A):
    for i in range(1, len(A)):
        if A[i - 1] > A[i]:
            return False
    return A[0] + A[(len(A) // 2)] + A[-1]


A = [int(x) for x in input().split()]
# print(f'sort전: {A}')


m_sort(A, 0, len(A) - 1)

print(check(A))
print(f'sort후: {A}')