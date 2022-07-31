target_str = input()
result = ""

for i in range(len(target_str)):
    if target_str[i].isupper():
        result += target_str[i].lower()
        continue
    result += target_str[i].upper()

print(result)