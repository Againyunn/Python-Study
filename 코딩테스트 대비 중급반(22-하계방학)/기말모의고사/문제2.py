n = int(input())
arr = list(map(int, input().split()))

this_max = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        # print(f"i:{i}, j:{j}")
        if j - i >= 2:
            this_max = max(this_max, arr[i] + arr[j])

print(this_max)