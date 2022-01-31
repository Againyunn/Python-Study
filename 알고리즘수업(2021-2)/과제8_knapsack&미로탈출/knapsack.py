
def fractional_knapsack(i, Size):
    global item_value, item_size, n

    # key=가성비, value=인덱스 형태로 dict에 저장
    bag = dict([[item_value[j] / (item_size[j] + 1), j] for j in range(n)])
    #bag = [[item_value[j] / (item_size[j] + 1), j] for j in range(n)]
    result = 0 #greedy 방식 이용(가성비 우선)

    # 가성비 순서로 정렬
    sort_by_value=sorted(bag.items())
    # sort_by_value = sorted(bag, key=lambda item_value_item_size: -item_value_item_size[0])
    # print(f'sort_by_value={sort_by_value}')

    # 가성비
    for i in sort_by_value:
        tmp=i[1]
        # 공간이 있으면 아이템 넣기
        if item_size[tmp] <= Size:
            Size -= item_size[tmp]
            result += item_value[tmp]
        # 물건의 무게가 공간보다 큰 경우 가능한 만큼 넣기(K(=남은 공간)*가성비)
        else:
            result += (K * i[0])
            print(f'i={i[0]}')
            break

    return result

def zero_one_knapsack(i, Size) :

    global item_size, item_value, x, tmp_max_value, answer, n

    #item을 모두 반영 or 가방이 꽉 찬 경우
    if i >= n or Size <= 0:
        return

    # 현재까지 선택한 item의 무게와 가치를 구하기
    value = sum(item_value[j] for j in range(0, i+1) if x[j] == 1)

    # x[i] = 1을 따라가야 하는 지 결정
    if item_size[i] <= Size:
        B = fractional_knapsack(i+1, Size - item_size[i]) #B = B(i+1)
        if value + item_value[i] + B > tmp_max_value:

            x[i] = 1
            # tmp_max_value 업데이트
            if value + item_value[i] > tmp_max_value:
                answer[:] = x[:]
                tmp_max_value = value + item_value[i]


            zero_one_knapsack(i+1, Size - item_size[i])

    # x[i]를 선택하지 않는다면?
    B = fractional_knapsack(i+1, Size)
    if tmp_max_value < value + B :
        x[i] = 0
        zero_one_knapsack(i+1, Size)

K = int(input()) # 가방 총 크기
n = int(input()) # 아이템 수

item_size = input().split() #아이템 크기
item_value = input().split() #아이템 가치

for i in range(n):
    item_size[i] = int(item_size[i])
    item_value[i] = int(item_value[i])

# 검토를 위한 변수
x = [0] * n
answer = [0] * n
tmp_max_value = 0

zero_one_knapsack(0, K)

max_value = 0 # 최대 가치 기록용 변수
for i in range(n):
    if answer[i] ==1:
        max_value += item_value[i]

print(max_value)


