def exp1(x,n): # O(n)
    result =1
    for i in range(1, n+1): #아니면 for i in range(n): 도 가능
        result*=x
    return result

def exp2(x,n): # O(n)
    if n ==0:
        return 1
    else:
        return x*exp2(x,n-1)

def exp3(x,n): # (2logn)
    if n==0:
        return 1
    elif(n%2==0):
        temp = exp3(x,n/2)
        return temp*temp
    else:
        return x*exp3(x, n-1)
