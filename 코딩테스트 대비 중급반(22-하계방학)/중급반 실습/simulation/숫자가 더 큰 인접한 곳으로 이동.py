dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, x, y = input().split()
n = int(n)
x = int(x) - 1
y = int(y) - 1

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

result = []
result.append(arr[x][y])

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

stop = False

while not stop:
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        stop = True

        # print(f"i: {i}")

        if in_range(nx, ny) and arr[x][y] < arr[nx][ny]:
            # print(f"arr[{nx}][{ny}]:{arr[nx][ny]}")
            result.append(arr[nx][ny])
            x, y = nx, ny
            stop = False
            break
            

print(*result)