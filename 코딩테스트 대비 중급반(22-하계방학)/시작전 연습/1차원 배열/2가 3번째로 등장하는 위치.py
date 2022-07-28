num = int(input())
arr = list(map(int, input().split()))
arr_len = len(arr)

total_count = 0 #현재 몇 번째 숫자인지
two_count = 0 #2가 몇 번 등장했는 지

for i in range(arr_len):
    total_count += 1
    if arr[i] == 2:
        two_count += 1
    if two_count == 3:
        break
print(total_count)