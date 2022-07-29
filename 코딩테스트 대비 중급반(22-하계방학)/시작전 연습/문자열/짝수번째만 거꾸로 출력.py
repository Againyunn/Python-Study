original = input()

result =""
for i in range(len(original) - 1, -1, -1):
    if i % 2 != 0:
        result += original[i]

print(result)