str1 = input()

change_char = str1[0]
target_char = str1[1]

result = ""
for i in range(len(str1)):
    if str1[i] == target_char :
        result += change_char
        continue
    
    result += str1[i]

print(result)