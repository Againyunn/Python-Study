def max_sum(A):
    P = []

    P.append(A[0])
    if len(A) > 0:
        for a in range(1, len(A)):
            P.append(P[a - 1] + A[a])

    max_num = P[0]
    P_num = len(P)
    for i in range(0, P_num):
        for j in range(i + 1, P_num):
            if i == 0:
                tmp = P[j] - P[0]
                if tmp > max_num:
                    max_num = tmp
            else:
                tmp = P[j] - P[i - 1]
                if tmp > max_num:
                    max_num = tmp

    if max_num < P[P_num - 1]:
        max_num = P[P_num - 1]

    return max_num


A = [int(x) for x in input().split()]
sol = max_sum(A)
print(sol)