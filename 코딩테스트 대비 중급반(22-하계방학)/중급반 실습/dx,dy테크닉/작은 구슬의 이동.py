# num, time = tuple(map(int, input().split()))

# x, y, now_dir = input().split()
# x = int(x)
# y = int(y)

# # 방향 U, R, D, L
# direction = ["U", "R", "L", "D"]
# dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]

# def in_range(x, y):
#     return 0 <= x and x < num and 0 <= y and y < num

# while time > 0:
#     dir_num = direction.index(now_dir)
#     nx, ny = x + dxs[dir_num], y + dys[dir_num]

#     if not in_range(nx, ny):
#         dir_num = 3 - dir_num
#         time -= 1
#         # continue

#     x, y = x + dxs[dir_num], y + dys[dir_num]
#     time -= 1
#     # if not in_range(x, y):
#     #     if x < 0:
#     #         x += 3
#     #     elif x >= num:
#     #         x -= 3
#     #     if y < 0:
#     #         y += 3
#     #     elif y >= num:
#     #         y -= 3
    
# print(x, y)

num, time = tuple(map(int, input().split()))
x, y, c_direction = tuple(input().split())

mapper = {
    'R':0,
    'D':1,
    'U':2,
    'L':3
}

x, y, move_direction = int(x) - 1, int(y) - 1, mapper[c_direction]

dxs = [0, 1, -1, 0]
dys = [1, 0, 0, -1]

def in_range(x, y):
    return 0 <= x and x < num and 0 <= y and y < num

for _ in range(time):
    nx, ny = x + dxs[move_direction], y + dys[move_direction]

    if in_range(nx, ny):
        x, y = nx, ny
    
    else:
        move_direction = 3 - move_direction

print(x + 1, y + 1)



# # 변수 선언 및 입력
# n, t = tuple(map(int, input().split()))
# x, y, c_dir = tuple(input().split()) # ("1", "2", "L")

# # 각 알파벳 별 방향 번호를 설정합니다.
# mapper = {
#     'R': 0,
#     'D': 1,
#     'U': 2,
#     'L': 3
# }
# x, y, move_dir = int(x) - 1, int(y) - 1, mapper[c_dir]

# dxs = [0, 1, -1,  0]
# dys = [1, 0,  0, -1]


# def in_range(x, y):
#     return 0 <= x and x < n and 0 <= y and y < n


# # simulation 진행
# for _ in range(t):
#     nx, ny = x + dxs[move_dir], y + dys[move_dir]
#     # 범위 안에 들어온다면 그대로 진행합니다.
#     if in_range(nx, ny):
#         x, y = nx, ny
#     # 벽에 부딪힌다면, 방향을 바꿔줍니다.
#     else:
#         move_dir = 3 - move_dir

# print(x + 1, y + 1)
