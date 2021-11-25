def solve(L, S):
    DP = [[0 for col in range(S+1)] for raw in range(L+1)] #DP결과 테이블을 저장할 임의의 빈 리스트

    for i in range(0, S+1): #각 자리 수가 1일 때의 각 수의 개수(1)를 DP에 기록
        DP[1][i] = 1

    if L == 1: #자리수가 1인 값을 입력 받았을 때
        if S<=9: #요구하는 자리들의 합이 9이하이면 해당 자리의 값(1)을 출력
            return DP[1][S]
        else: #10이상일 경우 False(연산불가) 반환
            return False

    # L자리수가 2부터 증가함에따라 S각 값의 합에 맞는 자리값의 합을 구한 뒤, DP에 저장
    for i in range(2, L+1):
        for j in range(S-1, -1, -1):
            # j - x 가(x>j)인 경우의 j - x 연산 시도 방지를 위해 모든 가능한 자리수의 경우를 조건절if로 분리하여 연산
            if j-9>=0:
                DP[i][j] = DP[i-1][j] + DP[i-1][j-1] + DP[i-1][j-2] + DP[i-1][j-3] + DP[i-1][j-4] + DP[i-1][j-5] + DP[i-1][j-6] + DP[i-1][j-7] + DP[i-1][j-8] + DP[i-1][j-9]
            elif j-8>=0:
                DP[i][j] =  DP[i-1][j] + DP[i-1][j-1] + DP[i-1][j-2] + DP[i-1][j-3] + DP[i-1][j-4] + DP[i-1][j-5] + DP[i-1][j-6] + DP[i-1][j-7] + DP[i-1][j-8]
            elif j-7>=0:
                DP[i][j] = DP[i-1][j] + DP[i-1][j-1] + DP[i-1][j-2] + DP[i-1][j-3] + DP[i-1][j-4] + DP[i-1][j-5] + DP[i-1][j-6] + DP[i-1][j-7]
            elif j-6>=0:
                DP[i][j] = DP[i-1][j] + DP[i-1][j-1] + DP[i-1][j-2] + DP[i-1][j-3] + DP[i-1][j-4] + DP[i-1][j-5] + DP[i-1][j-6]
            elif j-5>=0:
                DP[i][j] = DP[i-1][j] + DP[i-1][j-1] + DP[i-1][j-2] + DP[i-1][j-3] + DP[i-1][j-4] + DP[i-1][j-5]
            elif j-4>=0:
                DP[i][j] = DP[i-1][j] + DP[i-1][j-1] + DP[i-1][j-2] + DP[i-1][j-3] + DP[i-1][j-4]
            elif j-3>=0:
                DP[i][j] = DP[i-1][j] + DP[i-1][j-1] + DP[i-1][j-2] + DP[i-1][j-3]
            elif j-2>=0:
                DP[i][j] = DP[i-1][j] + DP[i-1][j-1] + DP[i-1][j-2]
            elif j-1>=0:
                DP[i][j] = DP[i-1][j] + DP[i-1][j-1]
            elif j>=0:
                DP[i][j] = DP[i-1][j]

            else:
                pass

    return DP[L][S-1]


L, S = [int(x) for x in input().split()]
print(solve(L, S)%2147483647)

#수행시간:
# O(n^2)