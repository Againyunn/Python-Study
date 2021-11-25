def print_IS(seq, x):
    for i in range(len(seq)):
        if x[i]:
            print(seq[i], end="")
        else:
            print("_", end="")
    print()

def LIS_DP(seq):
    num=len(seq)   #입력받은 리스트의 원소 개수 기록
    LIS=[0 for x in range(num)]
    S = [] #각 원소별 최대 부문자열을 임시로 담을 변화하는 리스트 (리스트 내의 모든 index가 for문 반복에 의해 입력되며 값을 비교)
    S_max = [] #최대 부문자열 리스트를 담을 리스트 (check값이 최대가 될 때에만 값이 갱신)
    LIS[0] =1 #부분자열 수의 최소 단위 1
    S.append(seq[0]) #최소
    S_max.append(seq[0])
    check_max =1 #최대 부문자열의 수를 담을 변수

    for i in range(1,num):
        LIS[i] = 1 #부문자열 수의 최소 단위 '1' 지정
        check = 1 #각 부문자열들의 수를 담을 변화하는 값

        for j in range(i-1, -1, -1):
            if seq[j] < seq[i]: #증가하는 부문자열인지 확인 후 최대 값을 변화하는 값으로 지정
                LIS[i] = max(LIS[i], LIS[j]+1)
                S.append(max(seq[i], seq[j]))
                check+=1 #추가된 부문자열의 수만큼 추가
        if check_max < check:#기존의 최대 부문자열의 수보다 현재 부문자열의 수가 더 크다면 값을 갱신
            check_max=check #최대부문자열의 수
            S_max=list(S) #최대부문자열

    return max(LIS), S_max


seq = input()  # 알파벳 소문자로만 구성된 string 하나가 입력된다
lis, x = LIS_DP(seq)
print(lis)

#점화식
# 4n^2 + 6n + 8

#수행시간
# O(n^2)