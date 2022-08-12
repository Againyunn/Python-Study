def Fibo(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return Fibo(n-2)+Fibo(n-1)

sol=Fibo(10)
print(sol)
