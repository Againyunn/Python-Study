num = int(input())
arr = []
tmp = []

#전체 숫자를 arr에 저장
for i in range(1, num ** 2 +1):
    tmp.append(i)

    if(i) % num == 0:
        arr.append(tmp)
        tmp = []

reversed_arr = []
#짝수행 뒤집기
for i in range(num):
    tmp = []
    if(i % 2) != 0:
        for j in range(num-1, -1, -1):
            tmp.append(arr[i][j])
        reversed_arr.append(tmp)
    else:
        reversed_arr.append(arr[i])

#각 행별 역순 출력
for i in range(num-1, -1, -1):
    tmp = []
    for j in range(num-1, -1, -1):
        tmp.append(reversed_arr[j][i])
    print(*tmp)