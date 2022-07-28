num = int(input())
arr = list(map(int, input().split()))

min_gap = abs(arr[1] - arr[0])
for i in range(1, num):
    this_gap = abs(arr[i - 1] - arr[i])
    if(min_gap > this_gap):
        min_gap = this_gap
print(min_gap)