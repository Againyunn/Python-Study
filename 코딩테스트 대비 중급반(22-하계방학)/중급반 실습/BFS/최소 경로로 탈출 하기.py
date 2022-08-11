from collections import deque
from re import X

X_LEN, Y_LEN = tuple(map(int, input().split()))

q = deque()

grid = [
    list(map(int, input().split()))
    for _ in range(X_LEN)
]

step = [
    [0 for _ in range(Y_LEN)]
    for _ in range(X_LEN)
]
visited = [
    [False for _ in range(Y_LEN)]
    for _ in range(X_LEN)
]

def in_range(x, y):
    return 0 <= x and x < X_LEN and 0 <= y and y < Y_LEN

def push(x, y, s):
    step[x][y]  = s
    visited[x][y] = True
    q.append((x, y))

def bfs():
    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy

            if in_range(new_x, new_y) and grid[new_x][new_y] != 0 and not visited[new_x][new_y]:
                push(new_x, new_y, step[x][y] + 1)
                # print(step[x][y])

push(0, 0, 0)
bfs()
if step[X_LEN - 1][Y_LEN - 1] != 0:
    print(step[X_LEN - 1][Y_LEN - 1])
else:
    print(-1)