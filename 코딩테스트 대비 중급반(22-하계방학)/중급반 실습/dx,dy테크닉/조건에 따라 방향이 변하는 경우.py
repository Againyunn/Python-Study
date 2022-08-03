# 방향을 바꿀 때 서로 반대인 방향의 인덱스끼리 합했을 때 각 좌우/상하 방향의 합이 동일하면 알고리즘 짜기 편하다
n = 5
x, y = 1, 2
dir_num = 2

dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


while keep_moving():
    nx, ny = x + dxs[dir_num], y + dys[dir_num]
    if not in_range(nx, ny):  # check whether position is out of grid
        dir_num = 3 - dir_num # change direction
    
    # move
    x, y = x + dxs[dir_num], y + dys[dir_num]
