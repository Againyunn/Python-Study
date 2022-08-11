from collections import deque

n, k = tuple(map(int, input().split()))

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [0] * n
    for _ in range(n)
]

command = []

for _ in range(k):
    command.append(tuple(map(int, input().split())))



q = deque()

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x, y):
    if not in_range(x, y):
        return False
    
    if grid[x][y] == 1 or visited[x][y]:
        return False
    
    return True

def push(x, y):

    visited[x][y] = 1
    q.append((x, y))

    # print(f"push: {x}{y}")

def bfs():
    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy

            if can_go(new_x, new_y):
                push(new_x, new_y)


for i in range(k):

    push(command[i][0] - 1 , command[i][1] - 1)
    bfs()

#테스트
# for i in range(n):
#     print(*grid[i])
# print()
# for i in range(n):
#     print(*visited[i])
# print()


result = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 1:
            result += 1

print(result)