n, m = tuple(map(int, input().split()))

arr =[
    list(map(int, input().split()))
    for _ in range(n)
]

result = 0

for i in range(n):
    tmp = arr[i][0]
    check = 1

    for j in range(1, n):
        print(f"tmp:{tmp}, arr[{i}][{j}]:{arr[i][j]}")
        if tmp == arr[i][j]:
            check += 1

        elif tmp != arr[i][j]:
            tmp = arr[i][j]
            check = 1

    if check >= m:
        result += 1
    
    print(f"check: {check}")

for j in range(n):
    tmp = arr[0][j]
    check = 1

    for i in range(1, n):
        print(f"tmp:{tmp}, arr[{i}][{j}]:{arr[i][j]}")
        if tmp == arr[i][j]:
            check += 1

        elif tmp != arr[i][j]:
            tmp = arr[i][j]
            check = 1

    if check >= m:
        result += 1

    print(f"check: {check}")

print(result)