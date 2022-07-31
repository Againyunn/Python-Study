target_str = input()
target_ascii = ord(target_str)

result = ""
if target_ascii == 97:
    result = "z"
else:
    result = chr(target_ascii - 1)

print(result)