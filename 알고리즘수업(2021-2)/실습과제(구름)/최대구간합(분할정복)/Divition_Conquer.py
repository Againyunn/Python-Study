def max_sum(A, left, right):
    # P = []
    #
    # P.append(A[0])
    # if len(A) > 0:
    #     for a in range(1, len(A)):
    #         P.append(P[a - 1] + A[a])
    half=(right+left)//2
    global max_num
    max_num=0



    if right//2-1 < half: #왼쪽 구역(half보다 작은)
        return max_sum(A, left, half-1)

    elif left*2+1 > half: #오른쪽 구역(half보다 큰)
        return max_sum(A, half, right) #half를 오른쪽 구역에 포함하여 연산

    else:
        if right==left: #1개 남은 경우
            return A[right]
        else: #2개 남은 경우
            return A[right]+A[left]


def example(A, left, right):

    #기본 조건
    if left == right:
        return A[left]

    half =  (left + right)//2

    left = float('-inf')
    right = float('-inf')

    sum_num=0
    check=half
    while check>=left: #for a in range(half, left, -1):
        sum_num += A[check]
        left = max(sum_num, left)
        check-=1


    sum_num=0
    check=half+1
    while check<=right:    # for b in range(half+1, right+1):
        sum_num += A[check]
        right = max(sum_num, right)
        check+=1

    remain=max(example(A, left, half), example(A, half+1, right))
    print(f'remain={remain}')

    return max(left + right, remain)

#########################


def fast_max_sum(lst, low, high):
    # 구간의 길이가 1인 경우
    if low == high: return lst[low]

    # 배열을 lst[low ~ mid], lst[mid+1 ~ high]로 나눈다.
    mid = (low + high) // 2

    # left, right, check = -1000, -1000, -1000
    left, right= float('-inf'),float('-inf')

    # lst[i ~ mid]의 최대 구간을 찾는다.
    lst_sum = 0
    for i in range(mid, low - 1, -1):
        lst_sum += lst[i]
        left = max(left, lst_sum)

    # lst[i ~ mid]의 최대 구간을 찾는다.
    lst_sum = 0
    for j in range(mid + 1, high + 1, 1):
        lst_sum += lst[j]
        right = max(right, lst_sum)

    # 최대 구간이 두 조각 중 하나에만 속해 있는 경우의 답을 재귀 호출로 찾는다.
    single = max(fast_max_sum(lst, low, mid), fast_max_sum(lst, mid + 1, high))

    # 두 경우 중 최대치를 반환한다.
    return max(left+ right, single)





	# A[left], ..., A[right] 중 최대 구간 합 리턴

A = [int(x) for x in input().split()]
# sol = max_sum(A, 0, len(A)-1)
# sol = example(A, 0, len(A)-1)
sol = fast_max_sum(A, 0 ,len(A)-1)
print(sol)