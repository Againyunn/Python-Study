n = int(input())

picked = []
visited = [False] * (n + 1)


def print_permutation():
    for elem in picked:
        print(elem, end=" ")
    print()


# 현재 curr_num 번째 위치에
# 1에서 n까지의 수 중
# 아직 등장하지 않은 수를 결정해보는 함수
def get_permutation(curr_num):
    if curr_num == n + 1:
        print_permutation()
        return

    for i in range(1, n + 1):
        if visited[i]:
            continue
        
        visited[i] = True
        picked.append(i)

        get_permutation(curr_num + 1)

        picked.pop()
        visited[i] = False


get_permutation(1)
