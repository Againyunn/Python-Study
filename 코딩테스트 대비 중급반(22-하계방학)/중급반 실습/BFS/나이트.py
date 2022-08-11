from collections import deque

initialized_ans = -1

# 변수 선언 및 입력
n = int(input())
r1, c1, r2, c2 = tuple(map(int, input().split()))
r1, c1, r2, c2 = r1 - 1, c1 - 1, r2 - 1, c2 - 1

# bfs에 필요한 변수들 입니다.
q = deque()
visited = [
    [False for _ in range(n)]
    for _ in range(n)
]
step = [                    # step[i][j] : 시작점으로부터 (i, j) 지점에 도달하기 위한 최단거리를 기록
    [0 for _ in range(n)]   
    for _ in range(n)       
]

ans = initialized_ans

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x, y):
    return in_range(x, y) and not visited[x][y]




def push(nx, ny, new_step):
    q.append((nx, ny))
    visited[nx][ny] = True
    step[nx][ny] = new_step # 시작점으로 부터의 최단거리 값도 갱신


# bfs
def find_min():
    global ans
    
    while q:
        x, y = q.popleft()

        dxs = [-2, -2, -1, -1,  1, 1,  2, 2]
        dys = [-1,  1, -2,  2, -2, 2, -1, 1]

        # 8방향을 확인
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if can_go(nx, ny):
                # 최단 거리는 이전 최단거리에 1이 증가하게 됩니다. 
                push(nx, ny, step[x][y] + 1)
    
    # 도착지에 가는 것이 가능할때만 답을 갱신해줍니다.
    if visited[r2][c2]:
        ans = step[r2][c2]

# 실행
push(r1, c1, 0)
find_min()

# 출력:
if ans == initialized_ans:  # 불가능한 경우라면 -1 출력
    ans = -1    

print(ans)



#초기 풀이

# from collections import deque

# #입력 값
# n = int(input())

# start_x, start_y, end_x, end_y = list(map(int, input().split()))

# #초기 셋팅
# grid = [
#     [0] * n 
#     for _ in range(n)
# ]

# visited = [
#     [0] * n
#     for _ in range(n)
# ]

# q = deque()
# cnt_q = deque()

# def in_range(x, y):
#     return 0 <= x and x < n and 0 <= y and y < n

# def can_go(x, y):
#     if not in_range(x, y):
#         return False
    
#     if visited[x][y] == 1:
#         return False
    
#     return True

# def push(x, y):

#     visited[x][y] = 1
#     q.append((x, y))
#     # print(f"push: {x}{y}")

# def cnt_push(c):
#     cnt_q.append(c)

# def bfs():
#     global stop, result, cnt, this_cnt

#     step = False

#     dxs = [1, 2, 2, 1, -1, -2, -2, -1]
#     dys = [-2, -1, 1, 2, 2, 1, -1, -2]

#     while q:
#         if stop:
#             break
        
#         x, y = q.popleft()
#         print(f"x, y: {x}, {y}")

#         if step:
#             if len(cnt_q) != 0:
#                 this_cnt = cnt_q.popleft()

#             else:
#                 cnt = this_cnt + 1
        
#         print(f"cnt_q: {cnt_q}")

#         for dx, dy in zip(dxs, dys):
#             new_x, new_y = x + dx, y + dy

#             if can_go(new_x, new_y):
#                 step = True

#                 push(new_x, new_y)

#                 if cnt != this_cnt:
#                     cnt_push(cnt)

#                 print(f"new_x, new_y: {new_x}, {new_y}")

#                 if new_x == end_x - 1 and new_y == end_y - 1 :
#                     stop = True
        
        
#         print()



# stop = False
# result = 0
# this_cnt = 1
# cnt = 1
# push(start_x - 1, start_y - 1)
# bfs()

# #테스트
# # for i in range(n):
# #     print(*grid[i])
# # print()
# # for i in range(n):
# #     print(*visited[i])
# # print()

# if cnt == 1:
#     print(-1)
# else:
#     print(cnt)

