std_num = int(input())
pass_num = 0
for i in range(std_num):
    this_std_arr = list(map(int, input().split()))
    this_std_avg = sum(this_std_arr) / 4
    result = 'fail'
    if this_std_avg >= 60:
        result = 'pass'
        pass_num += 1
    print(result)
print(pass_num)