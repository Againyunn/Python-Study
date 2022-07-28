num = int(input())

arr = [[1 for col in range(num)] for row in range(num)]

for i in range(1, num):
    for j in range(1, num):
        arr[i][j] = (arr[i - 1][j - 1] + arr[i][j - 1] + arr[i - 1][j])

for i in range(num):
    print(*arr[i])