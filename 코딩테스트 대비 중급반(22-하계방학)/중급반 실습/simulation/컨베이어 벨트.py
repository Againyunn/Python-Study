num , time = tuple(map(int, input().split()))

grid = [
    list(map(int, input().split()))
    for _ in range(2)
]


for _ in range(time):
    #한번 연산에 사용할 변수
    temp1 = grid[1][num - 1]
    temp2 = grid[0][num - 1]
    
    #1행연산
    for i in range(num - 1, 0 , -1):
        grid[0][i] = grid[0][i - 1]
    
    grid[0][0] = temp1
    
    #2행연산
    for j in range(num - 1, 0 , -1):
        grid[1][j] = grid[1][j - 1]
    
    grid[1][0] = temp2
    
print(*grid[0])
print(*grid[1])