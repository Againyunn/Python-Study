n, m = input().split()
n = int(n)
m = int(m)

arr1 = []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr1.append(tmp)

arr2 = []
for j in range(n):
    tmp = list(map(int, input().split()))
    arr2.append(tmp)

for i in range(n):
    tmp = []
    for j in range(m):
        if(arr1[i][j] == arr2[i][j]):
            tmp.append(0)
        else:
            tmp.append(1)
    print(*tmp)