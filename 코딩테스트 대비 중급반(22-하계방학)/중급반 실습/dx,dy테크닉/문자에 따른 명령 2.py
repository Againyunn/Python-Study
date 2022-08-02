#시계 방향일 때는
# dir_num = (dir_num + 1) % 4

#반시계 방향일 때는 
# dir_num = (dir_num - 1 + 4) % 4
# 음수 % 수 -> 나머지결과가 1이 나올 지, 3이 나올지 확신할 수 없고 각 언어별로 외워둘 필요도 없으니
# 애초부터 그런 문제 사항을 없애자

input_arr = input()
arr = []

watch = 3
x, y = 0, 0
# N, S, E, W
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


# direction = ["L", "R", "F"]

for i in input_arr:
    if i == "L":
        watch = (watch - 1 + 4) % 4
    elif i == "R":
        watch = (watch + 1) % 4
    elif i == "F":
        x += dx[watch]
        y += dy[watch]

print(x, y)


