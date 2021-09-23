def QuickSelect(L,k):
    p = L[0]
    S=[] #Small
    B=[] #Big
    M=[] #Medium

    M.append(p)
    for i in L:
        if i < p:
            S.append(i)
        elif i>p:
            B.append(i)
        else:
            #pass
            M.append(i)

    if len(S) >=k:
        return QuickSelect(S, k)
    elif len(S) + (len(M)-1) <k:
        return QuickSelect(B, k-len(S)-(len(M)-1))
    else:
        return p

N=list(map(int,input().split(' ')))
n=N[0]
k=N[1]

L=[]
# for i in range(n):
#     tmp=input().split(' ')
#     print('*')
#     L.append(tmp)
L=list(map(int,input().split()))

answer=QuickSelect(L,k)
print(answer)
