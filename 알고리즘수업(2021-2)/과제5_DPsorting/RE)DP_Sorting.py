def solve(A):
    num=len(A)
    DP = [[0 for col in range(num)] for row in range(num+1)]

    if num ==1:
        return 0

    for a in range(num+1):
        check=0
        if a <num: #A[n]의 원소를 갖는 경우 n == a
            index_num =A[a]

            i=0 #각 원소별 인덱스 지정을 위한 변수
            tmp_num = A[0]
            while i < num:
                if tmp_num >index_num:
                    tmp_num-=1
                    check+=1
                if tmp_num < index_num:
                    tmp_num+=1
                    check+=1
                if tmp_num == index_num:#다음 인덱스 이동
                    DP[a][i] = check
                    i += 1
                    try:
                        tmp_num = A[i]
                    except:
                        pass

        if a == num: #A내의 원소가 오름차순으로 되어 있는 지 확인용 + 앞 뒤의 원소와 맞추어 비교
            b=0
            tmp_num = A[0]
            while b < num-1:
                if b ==0:
                    if tmp_num>A[b+1]: #원소[0] 첫원소
                        tmp_num-=1
                        check+=1
                    else:
                        #print(f'a={a}, b={b}')
                        DP[a][b] = check
                        b += 1
                        tmp_num = A[b]
                        continue

                if 0<b<num-1: #원소[1~n-2]
                    if A[b - 1] <= tmp_num : #or tmp_num <= A[b + 1]
                        DP[a][b] = check
                        b += 1
                        tmp_num = A[b]
                        #print("*")
                        try:
                            if tmp_num > A[b + 1]:
                                tmp_num -= 1
                                check += 1
                                A[b] = tmp_num
                                #print("***")
                                #print(tmp_num)
                                continue
                        except:
                            continue

                    if tmp_num < A[b-1]:
                        tmp_num+=1
                        check+=1
                        A[b]=tmp_num
                        #print("**")
                        #print(tmp_num)
                        continue


                        #print(f"{b}*1")


                if num-1<=b:
                    if tmp_num<A[b-1]: #원소[n-1] 마지막 원소
                        tmp_num+=1
                        check+=1
                    else:
                        DP[a][b] = check
                        b += 1

    result=[]
    tmp=0
    # tmp2=0
    for c in range(num):
        result.append(DP[c][num-1])
        tmp+=DP[num-1][c]
        if c == num-1:
            result.append(tmp)
            #result.append(tmp2)
            # result.append(abs(tmp-tmp2))
    #print(DP)
    #print(result)
    answer = min(result)
    return answer

A=[int(x) for x in input().split()]
print(solve(A))