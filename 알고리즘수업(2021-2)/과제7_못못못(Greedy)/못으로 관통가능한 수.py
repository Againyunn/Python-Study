def stick_num(stick, n):
    result=[]
    index=0
    index_check=0

    while index< n-1:

        check = stick[index][index_check]
        tmp = 0

        for i in range(n):
            if stick[i][0] <= check and check <= stick[i][1]:
                tmp+=1

        result.append(tmp)
        if index_check==0:
            index_check=1
        else:
            index_check = 0
            index +=1
    return max(result)

n=int(input())
stick=[]
for i in range(n):
    stick.append(list(map(int, input().split())))
print(stick_num(stick, n))