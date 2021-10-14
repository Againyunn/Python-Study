def merge(A, i, j, k, l ):
    first_i=i #첫번째 연산용 i
    second_i=i #세번째 연산용 i
    set_i=i

    # second_j=j # 두번째 연산용 j
    # set_j=j
    #i~j , j~k
    tmp1=[]
    mid1=(first_i+k)//2
    j=mid1+1
    while first_i <= mid1 and j <= k:
        if A[first_i] <= A[j]:
            tmp1.append(A[first_i])
            # print(f'A[{first_i}]={A[first_i]}')
            first_i += 1

        else:
            tmp1.append(A[j])
            # print(f'A[{j}]={A[j]}')
            j += 1

    for a in range(first_i, mid1+1):
        # print(f'A[{a}]={A[a]}')
        tmp1.append(A[a])
    for b in range(j, k+1):
        # print(f'A[{b}]={A[b]}')
        tmp1.append(A[b])
    for c in range(set_i, k+1):
        # print(f'tmp1[{c-set_i}]={tmp1[c-set_i]}')
        A[c] = tmp1[c-set_i]


    #i~k, k~l
    tmp2 = []
    # mid2=(second_i+l)//2
    mid2=k
    k=mid2+1

    while second_i <= mid2 and k <= l:
        if A[second_i] > A[k]:
            tmp2.append(A[k])
            # print(f'A[{k}]={A[k]}')
            k += 1

        else:
            tmp2.append(A[second_i])
            # print(f'A[{second_i}]={A[second_i]}')
            second_i += 1

    for a in range(second_i, mid2+1):
        # print(f'A[{a}]={A[a]}')
        tmp2.append(A[a])
    for b in range(k, l+1):
        # print(f'A[{b}]={A[b]}')
        tmp2.append(A[b])
    for c in range(set_i, l+1):
        # print(f'tmp2[{c-set_i}]={tmp2[c-set_i]}')
        A[c] = tmp2[c-set_i]


def m_sort(A, first, last):
    if last-first <2:
        return


    oneThird=first+(last-first)//3
    twoThird=first+2*((last-first)//3)+1
    # if oneThird ==0:
    #     twoThird = 1
    #     print('twoThird=1')
    # else:
    #     twoThird=(first+last)//3*2

    # print(f'first={first}')
    # print(f'oneThird={oneThird}')
    # print(f'twoThird={twoThird}')
    # print(f'last={last}')

    m_sort(A, first, oneThird)
    # print(f'1={A}')
    m_sort(A, oneThird, twoThird)
    # print(f'2={A}')

    m_sort(A, twoThird, last)
    # print(f'3={A}')

    merge(A, first, oneThird, twoThird, last)
    print(f'merge={A}')
    # print(f'first={first}')
    # print(f'oneThird={oneThird}')
    # print(f'twoThird={twoThird}')
    # print(f'last={last}')






def check(A):
    for i in range(1, len(A)):
        if A[i - 1] > A[i]:
            return False
    return A[0] + A[(len(A) // 2)] + A[-1]


A = [int(x) for x in input().split()]
# print(f'sort전: {A}')


m_sort(A, 0, len(A) - 1)
#######

print(check(A))
# print(f'sort후: {A}')