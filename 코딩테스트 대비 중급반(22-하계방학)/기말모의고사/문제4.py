# from collections import deque

# n = int(input())

# arr = [
#     list(map(int, input().split()))
#     for _ in range(n)
# ]

# visited = [
#     [0] * n
#     for _ in range(n)
# ]

# q = deque()

# result = []

# this_turn_max = 0

# def in_range(x, y):
#     return 0 <= x and x < n and 0 <= y and y < n

# def can_go(x, y):
#     if not in_range(x, y):
#         return False
    
#     if visited[x][y] != 0:
#         return False
#     return True

# def push(x, y, c):
#     global this_turn_max
#     visited[x][y] = 1
#     q.append((x, y))
#     this_turn_max = max(this_turn_max, arr[x][y])


# def bfs():
#     # 하 / 우
#     dxs = [1, 0] 
#     dys = [0, 1]

#     global this_turn_max

#     while q:
#         # print(q)
#         x, y = q.popleft()
#         # print(f"after: {q}")
#         tmp = []


#         for dx, dy in zip(dxs, dys):
            
#             new_x, new_y = x + dx, y + dy

#             if can_go(new_x, new_y):
#                 tmp.append([new_x, new_y])

#                 # print(*tmp)
#                 #비교

#             if new_x == n - 1 and new_y == n - 1:
#                 # print("check")
#                 result.append(this_turn_max)
#                 this_turn_max = 0
            
#             # print(f"{new_x},{new_y} => this_turn_max:{this_turn_max}")

#         if len(tmp) == 0:
#             pass
        
#         elif len(tmp) == 1:
#             push(tmp[0][0], tmp[0][1])
        
#         else:
#             if arr[tmp[0][0]][tmp[0][1]] <= arr[tmp[1][0]][tmp[1][1]]:
#                 push(tmp[0][0], tmp[0][1])
#             else:
#                 push(tmp[1][0], tmp[1][1])
    
#     result.append(this_turn_max)
            
        
        


# push(0, 0)
# bfs()
# # print(result)
# print(max(result))


n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

max_cnt = 0
for i in range(n):
    for j in range(n - 2):
        for k in range(n):
            for l in range(n - 2):
                if i == k and abs(j - l) <= 3:
                        continue
                cnt1 = arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
                cnt2 = arr[k][l] + arr[k][l + 1] + arr[k][l + 2]
                max_cnt = max(max_cnt, cnt1 + cnt2)
print(max_cnt)