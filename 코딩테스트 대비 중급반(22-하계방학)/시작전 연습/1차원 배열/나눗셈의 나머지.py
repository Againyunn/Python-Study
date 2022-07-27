a, b = tuple(map(int, input().split()))

remainder_arr = [0] * 10
last = a
while last > 1:
    remainder_arr[last % b] += 1
    last //= b

total = 0
for i in remainder_arr:
    total += i ** 2

print(total)