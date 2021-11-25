def stick_num(stick, n):
    result=[]
    index=0

    stick.sort()

    while index< n-1:

        check_f = stick[index][0]
        check_l = stick[index][1]
        tmp = 0

        print(f'check_f={check_f}')
        print(f'check_l={check_l}')

        for i in range(n):
            # if 조건문 조절 필요
            # if (check_f <= stick[i][0] and stick[i][1] <= check_l) or (check_f==stick[i][1] and check_l==stick[i][0]):
                tmp+=1
                print(f'stick[{i}][0]={stick[i][0]}')
                print(f'stick[{i}][1]={stick[i][1]}')

        result.append(tmp)
        index+=1

    return max(result)

n=int(input())
stick=[]
for i in range(n):
    stick.append(list(map(int, input().split())))
# stick= list(map(int,stick))
print(stick_num(stick, n))