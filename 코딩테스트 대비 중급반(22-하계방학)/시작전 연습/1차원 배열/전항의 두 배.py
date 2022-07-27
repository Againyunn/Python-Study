a, b = input().split()
a = int(a)
b = int(b)
result = [a, b]
for i in range(2, 10):
    result.append(result[i-1] + 2 * result[i-2])
print(*result)