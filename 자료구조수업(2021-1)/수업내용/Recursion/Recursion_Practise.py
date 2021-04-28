def f(n):
    if n ==0:
        print(n)
        return
    else:
        print(n)
        f(n-1)
        print(n)

a=int(input())
f(a)
