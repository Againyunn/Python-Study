arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
arr3 = list(map(int, input().split()))
arr4 = list(map(int, input().split()))

total = arr1[0]
total += (arr2[0] + arr2[1])
total += (arr3[0] + arr3[1] + arr3[2])
total += (arr4[0] + arr4[1] + arr4[2] + arr4[3])

print(total)