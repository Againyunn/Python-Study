arr = list(map(int, input().split()))

target = 500
min_num = 1
max_num = 1000

for el in arr:
    if target > el:
        min_num = max(min_num, el)
    
    elif target < el:
        max_num = min(max_num, el)

print(f"{min_num} {max_num}")