def fibo(n):
    check=0
    if n == 0:
        return 1
    p =0
    f =1
    while check < n/2:
        check+=1
        p = p +f
        f = p +f
    if n%2 !=0:
        return p
    else:
        return f

n=input()
n=int(n)
print(fibo(n))