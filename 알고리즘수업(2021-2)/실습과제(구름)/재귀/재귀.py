def reverse(L, a):
    n = len(L)
    if a < n//2:
        L[a], L[n-1-a] = L[n-1-a], L[a]
        reverse(L, a+1)

L = list(input())  # 문자열을 입력받아 리스트로 변환
reverse(L, 0)
print(''.join(str(x) for x in L))