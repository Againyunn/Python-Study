arr = list(map(int, input().split()))
pre_elment = arr[0] #첫번째 인덱스 원소
for i in range(1, 10):
    if arr[i] % 3 == 0:
        print(pre_elment)
        break
    pre_elment = arr[i]