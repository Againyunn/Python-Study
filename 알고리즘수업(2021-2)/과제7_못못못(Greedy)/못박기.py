def pinning_num(stick, n):

    result=[]
    index=0
    index_check = 0

    while index < n-1:
        check = stick[index][index_check]
        count = 0

        for i in range(n):
            if stick[i][0] <= check and check <= stick[i][1]:
                count +=1
        result.append(count)

        if index_check==0:
            index_check = 1
        else:
            index_check = 0
            index +=1


    min_pin = 0
    re_sum = 0
    result.sort(reverse=True)
    re_index = 0


    while re_sum <= n-1 and re_index <= len(result):
        re_sum += result[re_index]
        re_index +=1
        min_pin +=1
    return min_pin

n=int(input())
stick=[]
for i in range(n):
    stick.append(list(map(int, input().split())))

print(pinning_num(stick, n))