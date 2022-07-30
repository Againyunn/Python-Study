target_str = input()
command = input()
go_left = 0
go_right = 0

for i in range(len(command)):
    if command[i] == "L":
        go_left += 1
    elif command[i] == "R":
        go_right += 1

go_command = go_left - go_right

result = ""
target_str_len = len(target_str)
real_command = abs(go_command) % target_str_len

if go_command > 0:
    for i in range(real_command, target_str_len):
        result += target_str[i]
    for j in range(real_command):
        result += target_str[j]

elif go_command < 0:
    for i in range(target_str_len - real_command, target_str_len):
        result += target_str[i]
    for j in range(target_str_len - real_command):
        result += target_str[j]

elif go_command == 0:
    result = target_str

print(result)
