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

def MoM(A, k):  # L의 값 중에서 k번째로 작은 수 리턴
    if len(A) == 1:  # no more recursion
        return A[0]
    i = 0
    S, M, L, medians = [], [], [], []
    while i + 4 < len(A):
        medians.append(find_median_five(A[i: i + 5]))
        i+=5

    if i < len(A) and i + 4 >= len(A):  # 마지막 그룹으로 5개 미만의 값으로 구성
        medians.append(find_median_five(A[i:]))

    mom = MoM(medians, len(medians)//2) #비교할 피봇값(mom 지정)

    for v in A:
        if v < mom:
            S.append(v) #작은쪽에 배치
        elif v > mom:
            L.append(v) #큰쪽에 배치
        else:
            M.append(v) #중간 값에 배치

    #S, M, B에서 k번째의 원소 찾기
    if len(S)>=k: #S안에 k번째 원소 있는 경우
        return MoM(S,k)
    elif len(S)+len(M)<k: #L안에 k번째 원소 있는 경우
        return MoM(L,k-(len(S)+len(M)))
    else: #비교 피봇값(mom)이 k번째 원소인 경우
        return mom


# n과 k를 입력의 첫 줄에서 읽어들인다
N=input().split()
n=int(N[0])
k=int(N[1])
# n개의 정수를 읽어들인다. (split 이용 + int로 변환)
A=list(map(int,input().split()))

print(MoM(A, k))