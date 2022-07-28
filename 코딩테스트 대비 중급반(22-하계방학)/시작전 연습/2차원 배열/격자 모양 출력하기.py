size, dot_num = tuple(map(int, input().split()))

#격자 생성
arr = [[0 for col in range(size)] for row in range(size)]

#점 입력받기
for i in range(dot_num):
    tmp_row, tmp_col = tuple(map(int, input().split()))
    arr[tmp_row - 1][tmp_col - 1] = tmp_row * tmp_col

#격자 출력
for j in range(size):
        print(*arr[j])