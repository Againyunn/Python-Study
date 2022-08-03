'''실습 예제
# 파이썬은 for문을 반복하며 동시에 n개의 list에서 동일한 인덱스의 원소를 한번에 뽑아낼 수 있다.
a = [[0, 0, 0, 1, 0],
     [0, 1, 1, 1, 0],
     [0, 0, 0, 0, 1],
     [1, 0, 1, 1, 1],
     [1, 0, 1, 1, 0]]

x, y = 2, 1
dxs, dys = [0, 1, 0, -1], [-1, 0, -1, 0]

cnt = 0

def in_range(x, y):
    return 0 <= x and x <5 and 0 <= y and y < 5

for dx, dy in zip(dxs, dys):
    nx, ny = x + dx, y + dy

    if in_range(nx, ny) and  a[nx][ny] == 1:
        # and/ or로 조건을 식별할 때 좌 -> 우 순서로 인식하므로 우선적으로 적용해야 할 조건을 반드시 먼저 써야 한다.
        cnt += 1
    # python에서 boolean True는 생략가능

print(cnt)


    # try, except는 코딩테스트에는 절대 사용하면 안된다.
    # out of index라는 정확한 문제로 인해 이슈가 발생한 것인지 특정하여 확신할 수 없다.
'''
# num = int(input())
# arr = []

# for _ in range(num):
#     arr.append(list(map(int, input().split())))

# def in_range(x, y):
#     if 0 <= x and x <num and 0 <= y and y < num:
#         return True
#     else:
#         return False

# dxs, dys = [0, 1, 0, -1], [-1, 0, -1, 0]
# result = 0

# for x in range(num):
#     for y in range(num):
#         cnt = 0
#         for dx, dy in zip(dxs, dys):
#             nx, ny = x + dx, y + dy

#             if in_range(nx, ny) == True and arr[nx][ny] == 1 and not(nx == x and ny == y):
#                 cnt += 1
        
#         if in_range(nx, ny) == True and cnt >= 3:
#             result += 1
#             print(x, y)

# print(result)

n = int(input())

# grid = [
#     [0, 1, 0, 1],
#     [0, 0, 1, 1],
#     [0, 1, 0, 1],
#     [0, 0, 1, 0]
# ]

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]



def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


# (x, y) 위치를 기점으로 인접한 칸에 있는 숫자 1의 
# 개수를 세줍니다.
ans = 0
for x in range(n):
    for y in range(n):
        dxs = [ 0, 0, -1, 1]
        dys = [-1, 1,  0, 0]

        cnt = 0
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and grid[nx][ny] == 1:
                cnt += 1
        
        # (x, y)와 인접한 칸에 있는 숫자 1의 개수
        if cnt >= 3:
            ans += 1

print(ans)
