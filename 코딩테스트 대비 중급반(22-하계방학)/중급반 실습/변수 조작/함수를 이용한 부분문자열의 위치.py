target = input()
sub_str = input()

tmp = ''
tmp2 = ''
idx = 0
result_idx = False
check = 0
real = False

for i in range(len(target)):
    if sub_str[idx] == target[i]:
        tmp += target[i]

        idx += 1
        check += 1

        # print(f"target[{i}]: {target[i]}")
        # print(f"i: {i}")

        if result_idx != False and tmp == sub_str:
            if idx == 0:
                result_idx = i
            real = True
            break
        continue
    
    if check > 0:
        tmp = ""
        check = 0
        idx = 0


if not real:
    result_idx = -1

print(result_idx)