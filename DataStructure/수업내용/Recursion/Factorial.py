#반복문으로 팩토리얼 구현
def FactorialRepeat(n):
    result=1
    for i in range(1,n+1):
        result *=i
    return result

#재귀문으로 팩토리얼 구현
def FactorialRecursion(n):
    if n==1:
        return 1
    else:
        return n * FactorialRecursion(n-1)