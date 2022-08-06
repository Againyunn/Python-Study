n = int(input())
x, y = 0, 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
direction = {
    'N':0,
    'E':1,
    'S':2,
    'W':3
}

time = 0
stop = False

for _ in range(n):
    command_direction, move = tuple(input().split())
    this_direction = direction[command_direction]
    move = int(move)

    for _ in range(move):
        x, y = x + dx[this_direction], y + dy[this_direction]
        time += 1
        
        # print(f"x: {x}, y: {y}")

        if x == 0 and y == 0:
            stop = True
            break
    if stop:
        break

if stop == False:
    time = -1

print(time)