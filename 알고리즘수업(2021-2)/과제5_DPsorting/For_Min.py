def ForMin(A):
    num=len(A)
    memo=list(A)
    result=A[0]
    check=1

    while check<num:
        result+=A[check]
        for i in range(num-check):
            memo[i] = min(memo[i], memo[i+1])
            result += memo[i]
        check+=1
    return result

A = [int(x) for x in input().split()]
print(ForMin(A))

######분석#####

# 문제 접근방식
# 4개의 원소를 입력받았을 때, 비교되는 항목:
# (0,0) (0,1) (0,2) (0,3) 1단계
#       (1,1) (1,2) (1,3) 2단계
#             (2,2) (2,3) 3단계
#                   (3,3) 4단계
# 이 남으며 각 n단계는 앞선 n-1단계의 해당 값들 중 더 작은 수가 저장된다.

# 알고리즘 소개
# num은 향후 알고리즘에 len(A)가 사용될 때 매번 A의 개수를 반환하는 연산을 방지하여 최소한의 수행시간을 위해 지정한 변수
# 각 단계별 해당되는 답을 저장하기 위한 임의의 리스트 memo를 생성
# 이때 memo에는 1단계부터 비교해야 하기 때문에, memo에 리스트 A의 원소를 모두 복사
# result는 결과값을 담는 변수로, DP알고리즘을 돌며 "전체합" 결과를 담기위한 변수
# check는 1단계의 값을 result에 담고, 각 단계별 연산 조작(num-check)을 위한 변수
# while문을 반복하며 (x , y)중 y의 변수를 통제하고,
# for문을 반복하며 (x, y)중 x의 변수를 통제하여 연산을 수행

# 원소의 개수가 4인 리스트를 입력받았을 떄를 가정하면,
# (0,0) (0,1) (0,2) (0,3) 1단계
#       (1,1) (1,2) (1,3) 2단계
#             (2,2) (2,3) 3단계
#                   (3,3) 4단계
# 만 수행하기에, O(nlogn)의 수행시간을 갖는다.