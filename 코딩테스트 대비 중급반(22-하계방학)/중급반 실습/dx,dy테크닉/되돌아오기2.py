x, y = 0, 0
direction = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

stop = False
time = 0

command = input()

for el in command:
    if el != 'F':
        if el == 'R':
            direction = (direction + 1) % 4
            
        elif el == 'L':
            direction = (direction - 1 + 4) % 4

        time += 1
    
    elif el == 'F':
        x, y = x + dx[direction], y + dy[direction]
        time += 1

        # print(f"x: {x}, y: {y}")

        if x == 0 and y == 0:
            stop = True
            break

if stop == False:
    time = -1

print(time)