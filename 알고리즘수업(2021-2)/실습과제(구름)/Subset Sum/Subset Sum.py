def print_subset(x):
    print([A[i] for i in range(len(x)) if x[i]])

def subset_sum(k):
    v_sum=0
    for i in range(len(A)):
        if x[i]==1:
            v_sum+=A[i]

    if k == len(A):
        if v_sum == S:
            print_subset(x)

    else:
        # code for x[k] = 1 and x[k] = 0
        if v_sum + A[k] <= S:
            x[k] = 1
            subset_sum(k+1)
        x[k] =0
        subset_sum(k+1)

A = list(set(int(x) for x in input().split())) #부분합을 찾을 리스트
A.sort()
S = int(input()) #합
x = [0]*len(A)
v_sum=0
subset_sum(0)