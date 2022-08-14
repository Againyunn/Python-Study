n = int(input())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

result = []

this_turn_max = 1

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


# 하 / 우
dxs = [1, 0] 
dys = [0, 1]

x = 0
y = 0

while x != n and y != n:
    tmp = []

    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy

        if in_range(new_x, new_y):
            tmp.append([new_x, new_y])
        
    if len(tmp) == 0:
        break
    
    elif len(tmp) == 1:
        result.append(this_turn_max)
        x, y = tmp[0][0], tmp[0][1]
    
    else:
        if arr[tmp[0][0]][tmp[0][1]] <= arr[tmp[1][0]][tmp[1][1]]:
            this_turn_max = max(this_turn_max, arr[tmp[0][0]][tmp[0][1]])
            x, y = tmp[0][0], tmp[0][1]
        else:
            this_turn_max = max(this_turn_max, arr[tmp[1][0]][tmp[1][1]])
            x, y = tmp[1][0], tmp[1][1]

print(*result)
ouput = max(result)
print(ouput)
