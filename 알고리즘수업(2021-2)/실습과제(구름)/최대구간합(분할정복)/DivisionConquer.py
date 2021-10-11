def max_sum(A, left, right):
    # 중간값
    half = (left + right) // 2

    # 원소가 1개인 경우 하나만을 반환
    if left==right:
        return A[left]

    left_max=-1000 #왼쪽 구간 최대값 변수
    right_max=-1000 #오른쪽 구간 최대값 변수
    #입력가능한 최소 값 -1000을 초기값으로 지정

    tmp=0
    check=half #시작값
    while check > left-1: #양쪽에 걸친 원소 중 왼쪽 구간 체크
        tmp+= A[check]
        left_max=max(left_max, tmp)
        check-=1

    tmp=0
    check=half+1 #시작값
    while check < right+1: #양쪽에 걸친 원소 중 오른쪽 구간 체크(
        tmp+= A[check]
        right_max=max(right_max, tmp)
        check+=1

    other=max(max_sum(A, left, half), max_sum(A, half + 1, right))

    answer=max(left_max+right_max, other)
    return answer

A = [int(x) for x in input().split()]
sol = max_sum(A, 0 ,len(A)-1)
print(sol)