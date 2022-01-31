chocolate=input().split()
N=int(chocolate[0])
M=int(chocolate[1])

cuts = (N - 1) + N * (M - 1)

print(cuts)