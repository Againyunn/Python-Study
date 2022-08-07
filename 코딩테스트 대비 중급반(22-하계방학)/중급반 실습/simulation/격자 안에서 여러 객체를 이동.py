n, g, t = input().split()
n = int(n)
g = int(g)
t = int(t)

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

count = [
    [0] * n
    for _ in range(n)
]

next_count = [
    [0] * n
    for _ in range(n)
]

#구슬의 위치 입력받기
for _ in range(g):
    x, y = tuple(map(int, input().split()))

    count[x - 1][y - 1] = 1

#함수들 정의
def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def get_next_pos(x, y):
    max = 0
    max_pos=(0,0)
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and arr[nx][ny] > max:
            max = arr[nx][ny]
            max_pos=(nx,ny)
    return max_pos

def g_move(x, y):
    next_x, next_y = get_next_pos(x, y)

    next_count[next_x][next_y] += 1

def move_all():
    for i in range(n):
        for j in range(n):
            next_count[i][j] = 0
    
    # print("before")
    for i in range(n):
        # print(*count[i])
        for j in range(n):
            if count[i][j] == 1:
                g_move(i, j)
    
    # print("after")
    for i in range(n):
        for j in range(n):
            count[i][j] = next_count[i][j]
        # print(*count[i])


for _ in range(t):
    move_all()

result = 0
# print("result")
for i in range(n):
    # print(*count[i])
    for j in range(n):
        if count[i][j] == 1:
            result += 1

print(result)