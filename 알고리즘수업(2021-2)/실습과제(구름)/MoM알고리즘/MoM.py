def find_median_five(A):
    B=list(A)

    check_A=0
    while len(B)>0:
        max_B = max(B)
        B.remove(max_B)
        if len(B)<=0:
            return max_B
        min_B = min(B)
        B.remove(min_B)

        len_B = len(B)
        if min_B == max_B:  # A 값이 1개인 경우
            return max_B
        elif len_B==0: #A 값이 2개인 경우 작은 값 반환
            return min_B

A=list(map(int,input().split()))
answer=find_median_five(A)
print(answer)

#
# def MoM(A, k):  # L의 값 중에서 k번째로 작은 수 리턴
#     if len(A) == 1:  # no more recursion
#         return A[0]
#     i = 0
#     S, M, L, medians = [], [], [], []
#     while i + 4 < len(A):
#         medians.append(find_median_five(A[i: i + 5]))
#
#     if i < len(A) and i + 4 >= len(A):  # 마지막 그룹으로 5개 미만의 값으로 구성
#         medians.append(find_median_five(A[i:]))
#
#     mom = MoM()
#     for v in A:
#         if v < mom:
#
#         elif v > mom:
#
#         else:
#
#     if:
#         return
#     elif:
#         return
#     else:
#         return mom


# n과 k를 입력의 첫 줄에서 읽어들인다
# n개의 정수를 읽어들인다. (split 이용 + int로 변환)
# print(MoM(A, k))