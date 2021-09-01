num_check = int(input())

for i in range(num_check):
    num = list(input().split())
    num = list(map(int,num))
    result = num[0] + num[1]
    print(f'Case #{i+1}: {num[0]} + {num[1]} = {result}')
    num = []