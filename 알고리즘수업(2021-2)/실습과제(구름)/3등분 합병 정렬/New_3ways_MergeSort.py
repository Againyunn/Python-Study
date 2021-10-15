def merge(A, i, j, k, l):
    #입력값의 가정: i<=j , j<k<=l
    #따라서 mid값은 j로 가정하고, 연산에 쓰일 k값은 k(j+1)그대로 적용
    #각 변수가 오버라이딩될 위험 방지를 위해 가감이 발생하는 변수는 따로 저장
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

    #1/3값 지정
    oneThird=first+(last-first)//3

    #2/3값 지정
    twoThird=first+2*((last-first)//3)+1

    #1/3씩 기준으로 3등분하여 각각 재귀 정렬
    m_sort(A, first, oneThird)
    m_sort(A, oneThird+1, twoThird)
    m_sort(A, twoThird+1, last)

    #1차 합병(처음~1/3 & 1/3+1~ 2/3)
    merge(A, first, oneThird, oneThird + 1, twoThird)
    #2차 합병(1차 합병 결과 & 2/3+1~끝)
    merge(A, first, twoThird, twoThird + 1, last)





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