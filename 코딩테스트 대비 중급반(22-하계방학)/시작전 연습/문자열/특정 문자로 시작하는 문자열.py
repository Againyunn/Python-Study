num = int(input())

arr = []
for i in range(num):
    arr.append(input())

key = input()

result = []
for i in arr:
    if( i[0] == key ):
        result.append(len(i))

avg_result = round(sum(result) / len(result), 2)
print(f"{len(result)} {avg_result:.2f}")
