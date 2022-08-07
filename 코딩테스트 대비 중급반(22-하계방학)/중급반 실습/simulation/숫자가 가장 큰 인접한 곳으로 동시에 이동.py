# (x, y) 위치에 있는 구슬을 움직입니다.
def move(x, y):
    # 그 다음 위치를 계산합니다.
    next_x, next_y = get_next_pos(x, y)

    # 그 다음 위치에 구슬의 개수를 1만큼 추가해줍니다.
    next_count[next_x][next_y] += 1

#step1
#구슬은 전부 한번씩 움직여 봅니다.
def move_all():
    #step1-1
    #그 다음 각 위치에서 구슬 개수를 전부 초기화해놓습닏.
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            next_count[i][j] = 0
    
    #step1-2
    #(i, j) 위치에 구슬이 있는 경우
    #움직임을 시도해보고, 그 결과를 전부 next_count에 기록합니다.
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if count[i][j] == 1:
                move(i, j)
    
    #step1-3
    #next_count 값을 count에 복사합니다.
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            count[i][j] = next_count[i][j]
