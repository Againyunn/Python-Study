n, t = tuple(map(int, input().split()))

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

def in_range(x, y):
    return 1 <= x and x <= n and 1 <= y and y <= n

def simulate():
    global curr_x, curr_y

    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    max_num = 0
    max_pos = (-1, -1)

    for dx, dy in zip(dxs, dys):
        next_x, next_y = curr_x + dx, curr_y + dy

        if in_range(next_x, next_y) and arr[next_x][next_y] > max_num:
            max_num = arr[next_x][next_y]
            max_pos = (next_x, next_y)
        
        curr_x, curr_y = max_pos
    
    for _ in range(t):
        simulate()
