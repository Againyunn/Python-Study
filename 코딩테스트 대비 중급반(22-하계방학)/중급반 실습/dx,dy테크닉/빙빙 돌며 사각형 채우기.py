n, m = tuple(map(int, input().split()))

# 격자 생성
grid = [
    [0] * m
    for _ in range(n)
]

# 방향 설정
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

# 초기값 지정
x, y = 0, 0
direction = 0 

# 시작 위치에 초기 값
grid[x][y] = 1

# 인덱스 범위 유효성 검사
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

# 2부터 i번까지 채우기
for i in range(2, n * m + 1):
    # 다음 위치값 연산
    nx, ny = x + dxs[direction], y + dys[direction]

    # 인덱스 범위 초과 시
    if not in_range(nx, ny) or grid[nx][ny] != 0:
        direction = (direction + 1) % 4

    # 현재 값의 위치 이동 및 격자에 값 채워 넣기
    x, y = x + dxs[direction], y + dys[direction]
    grid[x][y] = i

# 결과 출력
for i in range(n):
    print(*grid[i])



