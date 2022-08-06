global m
n, m = tuple(map(int, input().split()))
sequence = list(map(int, input().split()))

global result
result = 0

def calculate():
    global result, m

    while m > 0:
        result += sequence[m - 1]

        # 홀수인 경우
        if m % 2 != 0:
            m -= 1
        elif m % 2 == 0:
            m //= 2

    
calculate()
print(result)

