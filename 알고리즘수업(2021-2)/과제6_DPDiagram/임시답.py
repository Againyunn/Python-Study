def Diagram(B,n):
    n_num=len(n)
    curr = n_num -(B-1)
    curr_num = n_num -(B-1)
    check = 0

    curr_sum = []
    DP=[]
    # for a in range(B):
    while curr_num >0:
        tmp = 0
        print(f'curr_num = {curr_num}')
        print(f'curr = {curr}')
        print(f'check = {check}')

        while curr > 0 :
            tmp +=1
            print(tmp)
            curr_sum.append(tmp)
            curr-=1
        for i in range(n_num):
            DP_tmp=[]
            if i <tmp:
                DP_tmp.append()

        check +=1
        # curr =n -(B-1) -check
        # curr = n  - (B -1)
        # curr_num= n -(B-1)
        curr = n_num -(B-1) -check
        curr_num -= 1


    print(curr_sum)

check = list(map(int,input().split()))
B = check[0]
num = check[1]
n=[]
for i in range(num):
    n.append(int(input()))
Diagram(B,n)