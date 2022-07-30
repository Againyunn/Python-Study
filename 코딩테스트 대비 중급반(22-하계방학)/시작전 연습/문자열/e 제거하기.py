target_str = input()
count = 0
result = ""
for i in range(len(target_str)):
    if count == 0 and target_str[i] == "e":
        count += 1
        continue
    result += target_str[i]

print(result)