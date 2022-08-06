N, M = tuple(map(int, input().split()))
grid = [
    [0] * N
    for _ in range(N)
]

dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]
result = []

def in_range(x, y):
    return x >= 0 and x < N and y >= 0 and y < N

for _ in range(M):
    check = 0

    co_x, co_y = tuple(map(int, input().split()))
    co_x -= 1
    co_y -= 1

    grid[co_x][co_y] = 1

    for i in range(4):
        if in_range(co_x + dx[i], co_y + dy[i]) and grid[co_x + dx[i]][co_y + dy[i]]:
            check += 1
    
    if check == 3:
        result.append(1)
    
    else:
        result.append(0)

for el in result:
    print(el)